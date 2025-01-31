import zoneinfo

from celery import shared_task
from django_celery_beat.models import PeriodicTask, IntervalSchedule, CrontabSchedule

from apps.weather.models import Country
from apps.weather.services import get_weather_data_service

schedule, created = CrontabSchedule.objects.get_or_create(
    minute='0',
    hour='0',
    day_of_week='*',
    day_of_month='*',
    month_of_year='*',
    timezone=zoneinfo.ZoneInfo('Asia/Tashkent')
)

# schedule, interval_created = IntervalSchedule.objects.get_or_create(
#     every=60,
#     period=IntervalSchedule.SECONDS,
# )

periodic_task, periodic_created = PeriodicTask.objects.get_or_create(
    name='Send weather notify every start of the day',
    defaults={
        'interval': schedule,
        'task': 'weather.tasks.save_weather_data_in_db',
    }
)

if not periodic_task.enabled:
    periodic_task.enabled = True
    periodic_task.save()


@shared_task
def save_weather_data_in_db():
    try:
        countries = Country.objects.values('name').distinct()
        for country in countries:
            get_weather_data_service(country['name'])
    except Exception as ex:
        raise ex
