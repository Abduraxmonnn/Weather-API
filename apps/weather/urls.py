# Django
from django.urls import path, include
from rest_framework import routers

# Project
from apps.weather.api import WeatherListViewSet

router = routers.DefaultRouter()
router.register('', WeatherListViewSet)

urlpatterns = [
    path('', include(router.urls)),

    path('retrieve/', WeatherListViewSet.as_view({'get': 'retrieve'}), name='weather-retrieve'),
]
