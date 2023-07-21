import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm

def index(request):
    appid = '9e4cb6b0f7142cb39fbfd874f11ef662'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    if(request.method == 'POST'):
        form = CityForm(request.POST)
        if form.is_valid():
         form.save()
        else:
            print(form.errors)


    form = CityForm()

    cities = City.objects.all()

    all_cities = []

    for city in cities: 
        res = requests.get(url.format(city.name)).json()
        if res.get('main'):
            city_info = {
                'city': city.name,
                'temp': res["main"]["temp"], 
                'icon': res["weather"][0]["icon"],
                'error': False,
            }
        else:
            city_info = {
                'city': city.name,
                'error': True,
            }
        all_cities.append(city_info)

    context = {'all_info': all_cities, 'form': form}

    return render(request, 'weather/index.html', context)

        
    









