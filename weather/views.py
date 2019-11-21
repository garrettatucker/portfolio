from django.shortcuts import render, redirect
import requests
from .models import City
from .forms import CityForm
from django.contrib.auth.models import User

def index(request):
    

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=6f5ed34fa576791c7cd1e9a5dcfc866d'

    err_msg = ''
    message = ''
    if request.method == 'POST': # only true if form is submitted
        form = CityForm(request.POST) # add actual request data to form for processing

        if form.is_valid():
            new_city = form.cleaned_data['name'] #captures name of requested city
            existing_city_count = City.objects.filter(name=new_city, user=request.user).count() #checks to see if user has already added a specific city id

            if existing_city_count == 0:
                new_city_weather = requests.get(url.format(new_city)).json()
                if new_city_weather['cod'] == 200:
                    instance = form.save() #sets an instance for form
                    instance.user.set([request.user.pk]) #requests user id to weather model
                    instance.save() # will validate and save if validate
                else:
                    err_msg = 'City does not exist'
            else:
                err_msg = 'City already exists'
        if err_msg:
            message = err_msg
        else:
            message = 'City was added to your list'

    form = CityForm()

    cities = City.objects.filter(user=request.user) #return all the cities by specific user in the database

    weather_data = []

    for city in cities:

        city_weather = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types
        
        weather = {
            'city' : city.name,
            'temperature' : city_weather['main']['temp'],
            'description' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon']
        }

        weather_data.append(weather) #add the data for the current city into our list
    
    context = {
        'weather_data' : weather_data, 
        'form' : form,
        'message' : message,
        
        }

    return render(request, 'weather/index.html', context) #returns the index.html template

def delete_city(request, city_name):
    City.objects.filter(name=city_name, user=request.user.pk).delete() #deletes city, make sure to use filter  and request user pk
    return redirect('/weather')                                        #instead of get to avoid error for having multiple users