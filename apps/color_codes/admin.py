# Django
from django.contrib import admin

# Project
from apps.color_codes.models import ColorCodes


@admin.register(ColorCodes)
class ColorCodesAdmin(admin.ModelAdmin):
    list_display = ['category', 'name', 'hex_code', 'start_point', 'end_point']
