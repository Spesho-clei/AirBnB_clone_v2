"""test hbnb console"""
import os
import unittest
from io import StringIO
from unittest.mock import patch

import pep8

from console import HBNBCommand
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.engine.file_storage import FileStorage
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

class TestConsole(unittest.TestCase):
    """Test console"""
    
    def test_pep8_console(self):
        """Test that console.py conforms to PEP8."""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
    def test_docstrings_in_console(self):
        """Test docstrings"""
        self.assertIsNotNone(HBNBCommand.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)
        self.assertIsNotNone(HBNBCommand.do_count.__doc__)
    def test_do_create(self):
        """test do_create"""
        hb_command = HBNBCommand()

        # Test creating an instance of BaseModel
        with patch('sys.stdout', new=StringIO()) as fake_out:
            hb_command.onecmd('create BaseModel')
            output = fake_out.getvalue().strip()
            self.assertTrue(len(output) > 0)  # Ensure output is not empty

        # Test creating an instance of User with parameters
        with patch('sys.stdout', new=StringIO()) as fake_out:
            hb_command.onecmd('create User email="test@example.com" password="pwd"')
            output = fake_out.getvalue().strip()
            self.assertTrue(len(output) > 0)  # Ensure output is not empty

    # Test 'do_show' method
    def test_do_show(self):
        """test do_show"""
        hb_command = HBNBCommand()

        # Test showing an existing BaseModel instance
        with patch('sys.stdout', new=StringIO()) as fake_out:
            hb_command.onecmd('create BaseModel')
            output = fake_out.getvalue().strip()

            with patch('sys.stdout', new=StringIO()) as fake_out_show:
                hb_command.onecmd('show BaseModel {}'.format(output))
                output_show = fake_out_show.getvalue().strip()
                self.assertTrue(len(output_show) > 0)  # Ensure output is not empty

        # Test showing a non-existing instance
        with patch('sys.stdout', new=StringIO()) as fake_out:
            hb_command.onecmd('show BaseModel 12345')
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "** no instance found **")  # Ensure correct error message

if __name__ == '__main__':
    unittest.main()          
