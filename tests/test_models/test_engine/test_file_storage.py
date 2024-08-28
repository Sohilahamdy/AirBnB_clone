#!/usr/bin/python3

import unittest
import os
import json
import pep8

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        """Set up for the tests."""
        self.b1 = BaseModel()
        self.a1 = Amenity()
        self.c1 = City()
        self.p1 = Place()
        self.r1 = Review()
        self.s1 = State()
        self.u1 = User()
        self.storage = FileStorage()
        self.storage.save()

    def teardown(self):
        """Clean up after the tests."""
        if os.path.exists("file.json"):
            os.remove("file.json")
        del self.b1
        del self.a1
        del self.c1
        del self.p1
        del self.r1
        del self.s1
        del self.u1
        del self.storage

    def test_all(self):
        """Test the all() method of the FileStorage class."""
        obj = self.storage.all()
        self.assertIsNotNone(obj)
        self.assertEqual(type(obj), dict)

    def test_storage_empty(self):
        """Test that storage is not empty."""
        self.assertIsNotNone(self.storage.all())

    def test_storage_all_type(self):
        """Test that all() returns a dictionary."""
        self.assertEqual(dict, type(self.storage.all()))

    def test_new(self):
        """Test the new() method of the FileStorage class."""
        obj = self.storage.all()
        self.u1.id = 1234
        self.u1.name = "julien"
        self.storage.new(self.u1)
        key = "{}.{}".format(self.u1.__class__.__name__, self.u1.id)
        self.assertIsNotNone(obj[key])

    def test_check_json_loading(self):
        """Test that JSON file loads correctly."""
        with open("file.json") as f:
            dic = json.load(f)
            self.assertEqual(isinstance(dic, dict), True)

    def test_file_existence(self):
        """Test that the JSON file is created and not empty."""
        with open("file.json") as f:
            self.assertTrue(len(f.read()) > 0)

    def test_docstrings(self):
        """Check if docstrings are present in methods"""
        self.assertTrue(FileStorage.all.__doc__)
        self.assertTrue(hasattr(FileStorage, 'all'))
        self.assertTrue(FileStorage.new.__doc__)
        self.assertTrue(hasattr(FileStorage, 'new'))
        self.assertTrue(FileStorage.save.__doc__)
        self.assertTrue(hasattr(FileStorage, 'save'))
        self.assertTrue(FileStorage.reload.__doc__)
        self.assertTrue(hasattr(FileStorage, 'reload'))


if __name__ == '__main__':
    unittest.main()
