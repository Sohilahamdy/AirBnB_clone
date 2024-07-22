#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

class TestFileStorage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.storage = FileStorage()
        cls.file_path = 'file.json'
        cls.storage._FileStorage__file_path = cls.file_path

    @classmethod
    def tearDownClass(cls):
        try:
            os.remove(cls.file_path)
        except FileNotFoundError:
            pass

    def setUp(self):
        self.storage._FileStorage__objects = {}  # Clear storage before each test
        self.model = BaseModel()

    def test_new(self):
        """Test that new adds an object to storage"""
        self.storage.new(self.model)
        self.storage.save()
        all_objs = self.storage.all()
        self.assertEqual(len(all_objs), 1)

    def test_reload(self):
        """Test that reload properly loads objects from the file"""
        self.storage.new(self.model)
        self.storage.save()
        self.storage._FileStorage__objects = {}  # Clear storage
        self.storage.reload()
        all_objs = self.storage.all()
        self.assertEqual(len(all_objs), 1)

    def test_save(self):
        """Test that save properly saves objects to the file"""
        model2 = BaseModel()
        self.storage.new(self.model)
        self.storage.new(model2)
        self.storage.save()
        self.storage._FileStorage__objects = {}  # Clear storage
        self.storage.reload()
        all_objs = self.storage.all()
        self.assertEqual(len(all_objs), 2)

    def test_save_reload_new_instance(self):
        """Test saving and reloading with new instances"""
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.storage.new(obj1)
        self.storage.new(obj2)
        self.storage.save()
        self.storage._FileStorage__objects = {}  # Clear storage
        self.storage.reload()
        all_objs = self.storage.all()
        self.assertEqual(len(all_objs), 2)

if __name__ == "__main__":
    unittest.main()
