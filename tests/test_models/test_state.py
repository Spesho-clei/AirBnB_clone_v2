#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.state import State
import env
import unittest
from models.city import City
from models import storage

class test_state(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

@unittest.skipIf(not env.DBTYPE, "not testing file storage")
class TestStateDB(unittest.TestCase):
    """
    Test the State class with DBStorage
    """
    session = None

    def setUp(self):
        self.session = storage.get_session()
        self.session.query(State).delete()
        self.session.query(City).delete()
        self.session.commit()

    def tearDown(self):
        self.session.query(State).delete()
        self.session.query(City).delete()
        self.session.commit()

    def test_save(self):
        """
        Test save method
        """
        before = self.session.query(State).count()
        new_state = State(name="California")
        new_state.save()
        states = self.session.query(State).all()
        self.assertIsInstance(states[0], State)
        self.assertEqual(states[0].name, "California")
        self.assertEqual(before + 1, len(states))

    def test_get_cities(self):
        """
        Test cities property
        """
        new_state = State(name="California")
        new_state.save()

        with self.subTest("Test with no cities"):
            cities = new_state.cities
            self.assertIsInstance(cities, list)
            self.assertEqual(len(cities), 0)

if __name__ == '__main__':
    unittest.main()            
