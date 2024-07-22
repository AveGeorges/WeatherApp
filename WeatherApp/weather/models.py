from django.db import models

# Create your models here.
class Weather(models.Model):
    city = models.CharField(max_length=100)
    weather_now = models.CharField(max_length=20, default='Ясно')
    temperature = models.FloatField()
    apparent_temperature = models.FloatField()
    humidity = models.IntegerField()
    wind_speed = models.FloatField()
    precipitation_probability = models.IntegerField()

