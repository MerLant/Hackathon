import logging

logger = logging.getLogger(__name__)

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Логируем входящий запрос
        logger.info(f"Запрос: {request.method} {request.get_full_path()}")
        response = self.get_response(request)
        # Логируем статус ответа
        logger.info(f"Ответ: статус {response.status_code}")
        return response

    def process_exception(self, request, exception):
        # Логирование исключений с подробным стеком
        logger.error(f"Исключение при обработке запроса: {exception}", exc_info=True)
