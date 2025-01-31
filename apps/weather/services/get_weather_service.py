import requests
from django.conf import settings

from apps.weather.services import save_weather_to_db

BASE_URL = 'http://api.weatherapi.com/v1/'
TOKEN = settings.WEATHER_API_KEY


def get_weather_data_service(region: str) -> dict:
    error_response = {'status': 'error', 'message': 'default error'}

    try:
        r = requests.get(f'{BASE_URL}/current.json?key={TOKEN}&q={region}')
        r.raise_for_status()
        r_response = r.json()

        location_data = r_response['location']
        weather_data = r_response['current']

        data = {
            "region": location_data['region'],
            "country": location_data['country'],
            "lat": location_data['lat'],
            "lon": location_data['lon'],
            "temp_c": weather_data['temp_c'],
            "wind_kph": weather_data['wind_kph'],
            "cloud": weather_data['cloud'],
        }

        db_response = save_weather_to_db(data)
        city_weather = db_response.get('city_weather', None)

        if db_response['status'] == 'success':
            return {
                "name": location_data['region'],
                "country": location_data['country'],
                "lat": location_data['lat'],
                "lon": location_data['lon'],
                "temp_c": weather_data['temp_c'],
                "temp_color": city_weather.temp_color.hex_code,
                "wind_kph": weather_data['wind_kph'],
                "wind_color": city_weather.wind_color.hex_code,
                "cloud": weather_data['cloud'],
                "cloud_color": city_weather.cloud_color.hex_code,
            }

        return db_response

    except requests.exceptions.RequestException as e:
        error_response['message'] = str(e)
        return error_response
    except KeyError as e:
        error_response['message'] = f"Missing key in API response: {e}"
        return error_response
