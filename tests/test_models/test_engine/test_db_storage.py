#!/usr/bin/python3
"""Module for testing Place class with DBStorage"""
import datetime
import unittest
from models.place import Place
from models import storage
import env

def clear_db(conn):
    from models.engine.db_storage import classes
    cursor = conn.cursor()
    for table in classes:
        tablename = classes[table].__tablename__
        cursor.execute("DELETE FROM {}".format(tablename))
    conn.commit()

@unittest.skipIf(env.HBNB_TYPE_STORAGE != 'db', "not testing db storage")
class TestPlaceDB(unittest.TestCase):
    """Test cases for Place class with DBStorage"""

    def setUp(self):
        """Set up test environment"""
        self.conn = storage.get_session().get_bind()
        self.cursor = self.conn.cursor()
        clear_db(self.conn)

    def tearDown(self):
        """Tear down test environment"""
        self.cursor.close()
        self.conn.close()

    def test_created_place(self):
        """Test creating a new Place object"""
        new_place = Place(name="Test Place", city_id="12345")
        new_place.save()
        query = "SELECT * FROM places"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][1], "Test Place")
        self.assertEqual(result[0][3], "12345")

    def test_update_place(self):
        """Test updating a Place object"""
        new_place = Place(name="Test Place", city_id="12345")
        new_place.save()
        new_place.name = "Updated Place"
        new_place.save()
        query = "SELECT * FROM places"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][1], "Updated Place")

    def test_delete_place(self):
        """Test deleting a Place object"""
        new_place = Place(name="Test Place", city_id="12345")
        new_place.save()
        new_place_id = new_place.id
        new_place.delete()
        query = f"SELECT * FROM places WHERE id='{new_place_id}'"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        self.assertEqual(len(result), 0)

if __name__ == "__main__":
    unittest.main()
