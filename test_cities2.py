import unittest
from City_functions2 import city
class CityTest(unittest.TestCase):
    def test_city_country(self):
        test_name=city("shanghai","China",500000)
        self.assertEqual(test_name,"shanghai,China-population 500000")

    def test_city_country_population(self):
        test_name=city("shanghai","China",population=500000)
        self.assertEqual(test_name,"shanghai,China-population 500000")

unittest.main()