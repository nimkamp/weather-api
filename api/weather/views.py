# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import requests
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from decimal import *
from urlparse import urlparse, parse_qs
import json

# Create your views here.

ACCUWEATHER_URL = "http://127.0.0.1:5000/accuweather"
NOAA_URL = "http://127.0.0.1:5000/noaa"
WEATHERDOTCOM_URL = "http://127.0.0.1:5000/weatherdotcom"

def getCurrentAverageTemperature(latitude, longitude, filters = []):
    sum = 0

    if len(filters) > 0 and len(filters) <= 3:
        for filter in filters:
            filter = filter.lower()
            if filter == "accuweather":
                sum += getTempByAcccuweatherLocation(latitude, longitude)
            elif filter == "noaa":
                sum += getTempByNOAALocation(latitude, longitude)
            elif filter == "weatherdotcom":
                sum += getTempByWeatherdotcomLocation(latitude, longitude)
            else:
                print("Not a valid weather station.")
        return Decimal(sum)/len(filters)
    

def getTempByNOAALocation(latitude, longitude):
    o = urlparse(NOAA_URL)
    query = parse_qs(o.query)

    if (latitude >= -90 and latitude <= 90 and longitude >= -180 and longitude <= 180):
        if 'latlon' in query:
            query['latlon'] = str(latitude) + ',' + str(longitude)
        else:
            print("Nothing")
    else:
        print("Invalid latitude or longitude!")

    response = requests.get(NOAA_URL, params={'latlon': str(latitude) + ',' + str(latitude)})
    temperature = response.json()
    return float(temperature["today"]["current"]["fahrenheit"])

def getTempByAcccuweatherLocation(latitude, longitude):
    o = urlparse(ACCUWEATHER_URL)
    query = parse_qs(o.query)

    if (latitude >= -90 and latitude <= 90 and longitude >= -180 and longitude <= 180):
        if 'latitude' in query:
            query['latitude'] = str(latitude)
        elif 'longitude' in query:  
            query['longitude'] = str(longitude)
        else:
            print("Nothing")
    else:
        print("Invalid latitude or longitude!")

    response = requests.get(ACCUWEATHER_URL, params={'latitude': latitude, 'longitude': longitude})
    data = response.json()
    return float(data["simpleforecast"]["forecastday"][0]["current"]["fahrenheit"])

def getTempByWeatherdotcomLocation(latitude, longitude):
    if (latitude >= -90 and latitude <= 90 and longitude >= -180 and longitude <= 180):
        data = {
            'lat':latitude, 
            'lon':longitude
        }

        response = requests.post(url = WEATHERDOTCOM_URL, json={"lat": latitude, "lon": longitude})
        data = response.json()
        return float(data["query"]["results"]["channel"]["condition"]["temp"])

def weather(request):
    result = json.loads(request.body)
    return JsonResponse({"CurrentAverageTemperature":getCurrentAverageTemperature(result["latitude"], result["longitude"], result["filters"])})
