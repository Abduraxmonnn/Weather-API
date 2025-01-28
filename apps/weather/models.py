# Django
import uuid
from django.db import models

# Project
from apps.color_codes.models import ColorCodes


class Country(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'


class Region(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Region'
        verbose_name_plural = 'Regions'


class CityWeather(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='weather_country')
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='weather_region')
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lng = models.DecimalField(max_digits=9, decimal_places=6)
    temp = models.DecimalField(max_digits=5, decimal_places=2)
    temp_color = models.ForeignKey(ColorCodes, on_delete=models.SET_NULL, null=True, related_name='temp_color_weather')
    wind = models.DecimalField(max_digits=5, decimal_places=2)
    wind_color = models.ForeignKey(ColorCodes, on_delete=models.SET_NULL, null=True, related_name='wind_color_weather')
    cloud = models.DecimalField(max_digits=5, decimal_places=2)
    cloud_color = models.ForeignKey(ColorCodes, on_delete=models.SET_NULL, null=True,
                                    related_name='cloud_color_weather')

    created_date = models.DateField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.country.name

    class Meta:
        verbose_name = 'City Weather'
        verbose_name_plural = 'City Weathers'
