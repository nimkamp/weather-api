import unittest
import sys
sys.path.append('../')
from views import getCurrentAverageTemperature


class TestGetCurrentAverageTemperature(unittest.TestCase):

    def test_1_get_current_average_temperature(self):
        self.assertEqual(getCurrentAverageTemperature(44, 33, ["noaa", "accuweather", "weatherdotcom"]), 49)

    def test_2_get_current_average_temperature(self):
        self.assertEqual(getCurrentAverageTemperature(44, 33, ["noaa", "accuweather"]), 55)

if __name__ == '__main__': 
    unittest.main() 