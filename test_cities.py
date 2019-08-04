import unittest
from City_functions import city
class CityTest(unittest.TestCase):
    def test_city_country(self):
        test_name=city("shanghai","China")
        self.assertEqual(test_name,"shanghai,China")

unittest.main()