import os
import requests
from PIL import Image
from django.conf import settings
from django_filters.rest_framework import DjangoFilterBackend
from requests.exceptions import RequestException
from rest_framework import status, viewsets, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .models import Image as ImageModel
from .serializers import ImageSerializer

API_URL = settings.METADATA_API_URL


class ImageViewSet(viewsets.ModelViewSet):
    queryset = ImageModel.objects.all().order_by("id")
    serializer_class = ImageSerializer
    pagination_class = PageNumberPagination

    # Добавляем поддержку поиска
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['description', 'detected_objects', 'text']
    search_fields = ['description', 'detected_objects', 'text']

    def perform_create(self, serializer):
        """При создании изображения:
        1. Конвертируем в JPEG (если нужно)
        2. Получаем метаданные от API нейронки
        3. Обновляем модель и EXIF
        """
        instance = serializer.save()  # Сохраняем объект, но не отправляем в БД

        # Конвертируем изображение в JPEG
        image_path = instance.image.path
        image_path = self.convert_to_jpeg(image_path)  # Функция ниже

        try:
            # Отправляем изображение на API нейронки
            with open(image_path, "rb") as img_file:
                files = {"image": img_file}
                response = requests.post(API_URL, files=files)

            if response.status_code == 200:
                data = response.json()

                # Записываем полученные метаданные в БД
                instance.description = data.get("description", "No description received")
                instance.detected_objects = data.get("detected_objects", "No objects detected")
                instance.text = data.get("text", "No translated text")
                instance.save()

        except RequestException as e:
            return Response(
                {"error": f"API недоступно: {str(e)}"},
                status=status.HTTP_503_SERVICE_UNAVAILABLE
            )

    def convert_to_jpeg(self, image_path):
        """Преобразует изображение в JPEG (если это не JPEG) и перезаписывает файл."""
        try:
            with Image.open(image_path) as img:
                if img.format == "JPEG":
                    return image_path  # Уже в нужном формате

                # Генерируем новый путь (замена расширения на .jpg)
                new_path = os.path.splitext(image_path)[0] + ".jpg"

                # Если PNG/WebP — заливаем прозрачность белым
                if img.mode in ("RGBA", "P"):
                    img = img.convert("RGB")

                # Сохраняем как JPEG с качеством 90
                img.save(new_path, format="JPEG", quality=90)

                # Удаляем старый файл
                os.remove(image_path)

                return new_path

        except Exception as e:
            print(f"Ошибка конвертации изображения {image_path}: {e}")
            return image_path  # В случае ошибки возвращаем оригинальный путь
