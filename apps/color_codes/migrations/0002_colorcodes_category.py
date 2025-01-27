# Generated by Django 5.1.5 on 2025-01-27 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('color_codes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='colorcodes',
            name='category',
            field=models.CharField(choices=[('TEMPERATURE', 'Temperature'), ('WIND', 'Wind'), ('CLOUD', 'Cloud')], default='TEMPERATURE', max_length=11),
        ),
    ]
