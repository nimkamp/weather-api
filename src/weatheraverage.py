from decimal import *
import requests
from urlparse import urlparse, parse_qs
import json

ACCUWEATHER_URL = "http://127.0.0.1:5000/accuweather?latitude=44&longitude=33"
NOAA_URL = "http://127.0.0.1:5000/noaa?latlon=44,33"
WEATHERDOTCOM_URL = "http://127.0.0.1:5000/weatherdotcom"

def getCurrentAverageTemperature(latitude, longitude, filters = []):
    sum = 0
    if (len(filters) > 0 and len(filters) <= 3):

        for filter in filters:
            if filter.lower() == "accuweather":
                sum += getTempByAcccuweatherLocation(latitude, longitude)
            elif filter.lower() == "noaa":
                sum += getTempByNOAALocation(latitude, longitude)
            elif filter.lower() == "weatherdotcom":
                sum += getTempByWeatherdotcomLocation(latitude, longitude)
            else:
                print("Not a valid weather station.")
        return Decimal(sum)/Decimal(len(filters))
    

def getTempByNOAALocation(latitude, longitude):
    o = urlparse(NOAA_URL)
    query = parse_qs(o.query)
    url = o._replace(query=None).geturl()

    if (latitude >= -90 and latitude <= 90 and longitude >= -180 and longitude <= 180):
        if 'latlon' in query:
            query['latlon'] = str(latitude) + ',' + str(longitude)
        else:
            print("Nothing")
    else:
        print("Invalid latitude or longitude!")

    response = requests.get(url, params=query)
    temperature = response.json()
    return float(temperature["today"]["current"]["fahrenheit"])

def getTempByAcccuweatherLocation(latitude, longitude):
    o = urlparse(ACCUWEATHER_URL)
    query = parse_qs(o.query)
    url = o._replace(query=None).geturl()
    if (latitude >= -90 and latitude <= 90 and longitude >= -180 and longitude <= 180):
        if 'latitude' in query:
            query['latitude'] = str(latitude)
        elif 'longitude' in query:  
            query['longitude'] = str(longitude)
        else:
            print("Nothing")
    else:
        print("Invalid latitude or longitude!")

    response = requests.get(url, params=query)
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

    

# getTempByNOAALocation(44,33)
# getTempByAcccuweatherLocation(44,33)
# getTempByWeatherdotcomLocation(33.3, 44.4)
print(getCurrentAverageTemperature(44, 33, ["noaa", "accuweather", "weatherdotcom"]))