import requests as req

from apis import location_url, base_weather_url, weather_app_key, weather_app_id
from wt_exceptions import LocationException, WeatherException

output_file_path = "output/forecast.txt"


def weather_tracker(output):
    result = []

    geolocation = req.get(location_url)
    if geolocation.status_code != 200:
        raise LocationException
    loc_json = geolocation.json()
    city = loc_json['city']
    district = loc_json['district']
    latitude = '%.2f' % float(loc_json['latitude'])
    longitude = '%.2f' % float(loc_json['longitude'])

    full_weather_url = base_weather_url
    full_weather_url = full_weather_url.replace("lat", latitude)
    full_weather_url = full_weather_url.replace("long", longitude)
    full_weather_url = full_weather_url.replace("appid", weather_app_id)
    full_weather_url = full_weather_url.replace("appkey", weather_app_key)

    weather = req.get(full_weather_url)
    if weather.status_code != 200:
        raise WeatherException

    weather_json = weather.json()
    for day in weather_json['Days']:
        entry = {
            "Date": day['date'],
            "Max Temp (C)": day['temp_max_c'],
            "Min Temp (C)": day['temp_min_c'],
            "Summary": day['Timeframes'][0]['wx_desc']
        }
        result.append(entry)
    if output == 1:
        return [result, city, district]
    else:
        # print to text document
        file = open(output_file_path, 'w')
        file.write('***Forecast for {}, {}***\n'.format(city, district))
        for day in result:
            file.write("Date: {}\n".format(day['Date']))
            file.write("Max Temp (C): {}\n".format(day['Max Temp (C)']))
            file.write("Min Temp (C): {}\n".format(day['Min Temp (C)']))
            file.write("Summary: {}\n\n".format(day['Summary']))
        file.close()
        return []

