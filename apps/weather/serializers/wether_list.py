# Rest-Framework
from rest_framework import serializers

# Project
from apps.weather.models import CityWeather


class WeatherListSerializer(serializers.ModelSerializer):
    temp_color_code = serializers.ReadOnlyField()
    wind_color_code = serializers.ReadOnlyField()
    cloud_color_code = serializers.ReadOnlyField()
    country_name = serializers.ReadOnlyField()
    region_name = serializers.ReadOnlyField()

    class Meta:
        model = CityWeather
        # fields = '__all__'
        extra_fields = ['temp_color_code', 'wind_color_code', 'cloud_color_code', 'country_name', 'region_name']
        exclude = ('temp_color', 'wind_color', 'cloud_color', 'country', 'region')


class MultipleWeathersListSerializer(serializers.ModelSerializer):
    countries = serializers.ListSerializer(child=serializers.CharField())
