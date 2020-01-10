from weather_tracker import weather_tracker, output_file_path
from wt_exceptions import WeatherException, LocationException


def check_selection_value(value):
    return value in [1, 2]


if __name__ == '__main__':
    print("Welcome to the Automatic Weather Machine! We find your location (Based on IP Address) and tell you the "
          "weather for your area for the week")

    output = None

    try:
        print('1 - Print to Console')
        print('2 - Output to TXT File')
        while output is None or type(output) != int or output > 2 or output < 1:
            try:
                output = int(input("Output Selection: "))
                if not check_selection_value(output):
                    output = None
                    print("Provide a valid selection for output!")
            except ValueError:
                print("{} is not a number, please enter a number only".format(output))
        result = weather_tracker(output)
        if len(result) != 3:
            print('You can find your forecast in the file: {}'.format(output_file_path))
        else:
            forecast = result[0]
            city = result[1]
            district = result[2]
            print("Here is the forecast for {}, {}:".format(city, district))
            for day in forecast:
                print(day)
    except (LocationException, WeatherException) as error:
        print(error.args[0])
