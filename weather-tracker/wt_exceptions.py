class LocationException(Exception):
    def __init__(self):
        Exception.__init__(self, "Problem determining user's location")


class WeatherException(Exception):
    def __init__(self):
        Exception.__init__(self, "Problem retrieving the weather information for your area!")