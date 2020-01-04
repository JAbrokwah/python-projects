import requests as req

from apis import location_url, base_weather_url
from wt_exceptions import LocationException, WeatherException


def weather_tracker():
    geolocation = req.get(location_url)
    if geolocation.status_code != 200:
        raise LocationException

    loc_json = geolocation.json()
    city = loc_json['city']
    district = loc_json['district']
    latitude = loc_json['latitude']
    longitude = loc_json['longitude']

    full_weather_url = base_weather_url
    full_weather_url += "&lat={}&lon={}".format(latitude, longitude)

    weather = req.get(full_weather_url)
    if weather.status_code != 200:
        raise WeatherException

    weather_json = weather.json()
    return weather_json['forecast'], city, district

