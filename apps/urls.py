# Django
from django.urls import path, include

urlpatterns = [
    path('user/', include('apps.user.urls')),
    path('weather/', include('apps.weather.urls'))
]
