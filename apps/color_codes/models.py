# Django
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class ColorCodes(models.Model):
    class ColorCategory(models.TextChoices):
        TEMPERATURE = 'TEMPERATURE', _('Temperature')
        WIND = 'WIND', _('Wind')
        CLOUD = 'CLOUD', _('Cloud')

    start_point = models.IntegerField(validators=[MinValueValidator(-100), MaxValueValidator(99)])
    end_point = models.IntegerField(validators=[MinValueValidator(-99), MaxValueValidator(100)])
    category = models.CharField(max_length=11, choices=ColorCategory.choices, default=ColorCategory.TEMPERATURE)
    name = models.CharField(max_length=255)
    temp_name = models.CharField(max_length=255, blank=True, null=True)
    hex_code = models.CharField(max_length=100)

    def get_color_code(self, value):
        color_code = self.objects.filter(start_point__lte=value, end_point__gte=value).first()
        return color_code

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Color Codes'
        verbose_name_plural = 'Colors Codes'
        unique_together = [['name', 'hex_code']]
