import requests
from django.shortcuts import render
from .models import Weather
from .forms import CityForm

def index(request):
    form = ''
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']

            response_city = requests.get(f'https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&language=ru&format=json')
            data_city = response_city.json()

            latitude = data_city['results'][0]['latitude']
            longitude = data_city['results'][0]['longitude']

            response_weather = requests.get(f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}'
                                           f'&current=temperature_2m,relative_humidity_2m,apparent_temperature,wind_speed_10m,precipitation_probability,weather_code')
            data_weather = response_weather.json()
            weather_now = 'Ясно'
            weather_code = data_weather['current']['weather_code']
            if weather_code == 0:
                weather_now = 'Ясно'
            elif weather_code == 1 or weather_code == 2 or weather_code == 3:
                weather_now = 'Облачно'
            elif weather_code == 45 or weather_code == 48 or weather_code == 51 or weather_code == 53 or weather_code == 55 or weather_code == 56:
                weather_now = 'Небольшой дождь'
            elif weather_code == 57 or weather_code == 61 or weather_code == 63 or weather_code == 66 or weather_code == 80:
                weather_now = 'Дождь'
            elif weather_code == 65 or weather_code == 67 or weather_code == 63 or weather_code == 81 or weather_code == 82:
                weather_now = 'Сильный дождь'
            elif weather_code == 71 or weather_code == 73 or weather_code == 75 or weather_code == 77 or weather_code == 85 or weather_code == 86:
                weather_now = 'Снег'
            temperature = data_weather['current']['temperature_2m']
            relative_humidity = data_weather['current']['relative_humidity_2m']
            apparent_temperature = data_weather['current']['apparent_temperature']
            wind_speed = data_weather['current']['wind_speed_10m']
            precipitation_probability = data_weather['current']['precipitation_probability']

            Weather.objects.create(city=city, weather_now=weather_now, temperature=temperature, apparent_temperature=apparent_temperature,
                                   humidity=relative_humidity, wind_speed=wind_speed, precipitation_probability=precipitation_probability)
        else:
            form = CityForm()

    weathers = Weather.objects.all()
    context = {
        'form': form,
        'weathers': weathers
    }
    return render(request, 'weather/index.html', context)