#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.city import City
from models.state import State
import env
import unittest

class test_City(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

@unittest.skipIf(env('HBNB_TYPE_STORAGE') != 'db', "Not testing DBStorage")
class TestCityDB(unittest.TestCase):
    def setUp(self):
        # Perform setup actions: e.g., establish database connection
        self.session = storage.get_session()

    def tearDown(self):
        # Clean up after the test
        self.session.close()

    def test_save_city(self):
        # Test the save method for City class
        initial_city_count = self.session.query(City).count()

        # Create a new state and save it
        new_state = State(name="California")
        new_state.save()

        # Create a new city associated with the state and save it
        new_city = City(name="San Francisco", state_id=new_state.id)
        new_city.save()

        # Retrieve cities from the database
        city_count_after_save = self.session.query(City).count()
        cities = self.session.query(City).all()

        # Assertions
        self.assertEqual(initial_city_count + 1, city_count_after_save)
        self.assertIsInstance(cities[0], City)
        self.assertEqual(cities[0].name, "San Francisco")
        self.assertEqual(cities[0].state_id, new_state.id)

if __name__ == '__main__':
    unittest.main()        
