import unittest
import sys
sys.path.append('../src')
from weatheraverage import getCurrentAverageTemperature


class TestGetCurrentAverageTemperature(unittest.TestCase):

    def setUp(self):
        pass

    def test(self):
        self.assertTrue(True)

    def test_1_weather_average(self):
        self.assertEqual(getCurrentAverageTemperature(44, 33, ["noaa", "accuweather", "weatherdotcom"]), 49)

    def test_2_weather_average(self):
        self.assertEqual(getCurrentAverageTemperature(44, 33, ["noaa", "accuweather"]), 55)

if __name__ == '__main__': 
    unittest.main() 