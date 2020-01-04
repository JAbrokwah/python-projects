from weather_tracker import weather_tracker
from wt_exceptions import WeatherException, LocationException

if __name__ == '__main__':
    print("Welcome to the Automatic Weather Machine! We track you and tell you the weather for the week")

    try:
        forecast, city, district = weather_tracker()
        print("Here is the forecast for {}, {}:".format(city, district))
        print(forecast)
    except (LocationException, WeatherException) as error:
        print(error.args[0])