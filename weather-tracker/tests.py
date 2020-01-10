import unittest

from weather_tracker import weather_tracker, output_file_path


class WeatherTrackerTests(unittest.TestCase):
    def test_my_location(self):
        i_live_in = "Toronto"
        result = weather_tracker(1)
        self.assertEqual(3, len(result))
        self.assertEqual(result[1], i_live_in)

    def test_txt_output(self):
        expected_line_count = 37

        # empty txt file
        open(output_file_path, 'w').close()

        # run to output to file
        result = weather_tracker(2)

        actual_count = 1
        with open(output_file_path, 'r') as f:
            for line in f:
                actual_count += 1
        self.assertEqual(expected_line_count, actual_count)


if __name__ == '__main__':
    unittest.main()
