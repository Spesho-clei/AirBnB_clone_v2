#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.user import User
import unittest
import env

class test_User(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.password), str)

@unittest.skipIf(not env.DBTYPE, "not testing file storage")
class TestUserDB(unittest.TestCase):
    """
    Test the User class with DBStorage
    """
    session = None

    def setUp(self) -> None:
        from models import storage
        self.session = storage.get_session()
        self.session.query(User).delete()
        self.session.commit()

    def tearDown(self) -> None:
        self.session.query(User).delete()
        self.session.commit()

    def test_save(self):
        """
        Test save method
        """
        before = self.session.query(User).count()
        new_user = User(
            email="test@gmail.com",
            password="test",
            first_name="test",
            last_name="test"
        )
        new_user.save()
        after = self.session.query(User).count()

        # Check if count increased after saving
        self.assertEqual(before + 1, after)

        # Check if the saved user exists in the database
        users = self.session.query(User).all()
        self.assertTrue(new_user in users)

        # Check if attributes are correctly stored
        saved_user = self.session.query(User).filter_by(email="test@gmail.com").first()
        self.assertIsNotNone(saved_user)
        self.assertEqual(saved_user.first_name, "test")
        self.assertEqual(saved_user.last_name, "test")

if __name__ == '__main__':
    unittest.main()        
