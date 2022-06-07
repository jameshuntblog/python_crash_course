# test_cities.py

import unittest
from city_functions import get_formatted_city_country

class Test_Cities(unittest.TestCase):
    """Tests for 'city_functions.py'."""
    
    def test_city_country(self):
        formatted_name = get_formatted_city_country('sheboygan', \
            'united states')
        self.assertEqual(formatted_name, 'Sheboygan, United States')

    def test_city_country_population(self):
        formatted_name = get_formatted_city_country('santiago', \
            'chile',population=5000000)
        self.assertEqual(formatted_name, 'Santiago, Chile – '\
            'Population 5000000')

if __name__ == '__main__':
    unittest.main()