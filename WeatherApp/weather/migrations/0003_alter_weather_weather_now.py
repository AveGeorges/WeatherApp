# Generated by Django 5.0.7 on 2024-07-21 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0002_weather_weather_now'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weather',
            name='weather_now',
            field=models.IntegerField(default='Ясно'),
        ),
    ]
