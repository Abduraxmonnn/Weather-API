# Django
from django.db.models import F, Subquery, OuterRef

# Rest-Framework
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

# Project
from apps.weather.models import CityWeather
from apps.color_codes.models import ColorCodes
from apps.weather.serializers import WeatherListSerializer


def format_weather_response(weather):
    return {
        "name": weather.region_name,
        "country": weather.country_name,
        "lat": weather.lat,
        "lon": weather.lng,
        "temp_c": weather.temp,
        "temp_color": weather.temp_color_code,
        "wind_kph": weather.wind,
        "wind_color": weather.wind_color_code,
        "cloud": weather.cloud,
        "cloud_color": weather.cloud_color_code,
    }


class WeatherListViewSet(viewsets.ModelViewSet):
    model = CityWeather
    queryset = (model.objects.all()
    .select_related('country', 'region', 'temp_color', 'wind_color', 'cloud_color')
    .annotate(
        temp_color_code=Subquery(
            ColorCodes.objects.filter(pk=OuterRef('temp_color')).values('hex_code')[:1]
        ),
        wind_color_code=F("wind_color__hex_code"),
        cloud_color_code=F("cloud_color__hex_code"),
        country_name=F("country__name"),
        region_name=F("region__name")
    ))
    serializer_class = WeatherListSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        formatted_data = [format_weather_response(weather) for weather in queryset]

        return Response(formatted_data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        try:
            uuid = request.query_params.get('uuid')  # getlist() to get several params with same name
            if not uuid:
                return Response({
                    "status": "error",
                    "message": "UUID is required",
                }, status=status.HTTP_400_BAD_REQUEST)

            queryset = self.get_queryset().filter(uuid=uuid)
            weather = get_object_or_404(queryset)

            formatted_data = format_weather_response(weather)

            return Response(formatted_data, status=status.HTTP_200_OK)

        except CityWeather.DoesNotExist:
            return Response({
                "status": "error",
                "message": "Weather record does not exist",
            }, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({
                "status": "error",
                "message": str(e),
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=['post'], url_path='retrieve-multiple')
    def retrieve_multiple(self, request, *args, **kwargs):
        try:
            uuids = request.data.get('countries', [])

            if not uuids:
                return Response({
                    "status": "error",
                    "message": "At least one Country is required",
                }, status=status.HTTP_400_BAD_REQUEST)

            queryset = self.get_queryset().filter(uuid__in=uuids)

            if not queryset.exists():
                return Response({
                    "status": "error",
                    "message": "No matching records found",
                }, status=status.HTTP_404_NOT_FOUND)

            formatted_data = [format_weather_response(weather) for weather in queryset]

            return Response(formatted_data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                "status": "error",
                "message": str(e),
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
