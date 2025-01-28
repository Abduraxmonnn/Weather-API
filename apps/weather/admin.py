# Django
from django.contrib import admin

# Project
from apps.weather.models import Country, Region, CityWeather


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(CityWeather)
class CityWeatherAdmin(admin.ModelAdmin):
    list_display = ['id', 'country__name']
