from django.db import IntegrityError

from apps.weather.models import CityWeather, Country, Region, ColorCodes


def save_weather_to_db(weather_data):
    try:
        country_obj, country_created = Country.objects.get_or_create(name=weather_data['country'])
        region_obj, region_created = Region.objects.get_or_create(name=weather_data['region'])

        temp_color = ColorCodes.objects.get_color_code(value=weather_data['temp_c'],
                                                       category=ColorCodes.ColorCategory.TEMPERATURE)
        wind_color = ColorCodes.objects.get_color_code(value=weather_data['wind_kph'],
                                                       category=ColorCodes.ColorCategory.WIND)
        cloud_color = ColorCodes.objects.get_color_code(value=weather_data['cloud'],
                                                        category=ColorCodes.ColorCategory.CLOUD)

        city_weather, created = CityWeather.objects.get_or_create(
            temp=weather_data['temp_c'],
            temp_color=temp_color,
            wind=weather_data['wind_kph'],
            wind_color=wind_color,
            cloud=weather_data['cloud'],
            cloud_color=cloud_color,
            defaults={
                'country': country_obj,
                'region': region_obj,
                'lat': weather_data['lat'],
                'lng': weather_data['lon'],
            }
        )

        if not created:
            city_weather.temp = weather_data['temp_c']
            city_weather.temp_color = temp_color
            city_weather.wind = weather_data['wind_kph']
            city_weather.wind_color = wind_color
            city_weather.cloud = weather_data['cloud']
            city_weather.cloud_color = cloud_color
            city_weather.save()

        return {
            'status': 'success',
            'message': 'Weather data saved successfully',
            'city_weather': city_weather
        }

    except IntegrityError as e:
        return {'status': 'error', 'message': f"Database integrity error: {str(e)}"}
    except Exception as e:
        return {'status': 'error', 'message': f"Unexpected error: {str(e)}"}
