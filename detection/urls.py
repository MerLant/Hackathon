from django.urls import path, include
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

from .views import ImageViewSet

router = DefaultRouter()
router.register('images', ImageViewSet, basename='images')

urlpatterns = [
    path('', include(router.urls)),
]
