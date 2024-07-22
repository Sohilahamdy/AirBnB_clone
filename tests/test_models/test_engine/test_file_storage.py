#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os

class TestFileStorage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Create a temporary file for testing and clear the storage"""
        cls.storage = FileStorage()
        cls.file_path = 'test_file.json'
        cls.storage._FileStorage__file_path = cls.file_path
        cls.storage._FileStorage__objects = {}  # Clear the storage

    @classmethod
    def tearDownClass(cls):
        """Remove the test file after all tests"""
        try:
            os.remove(cls.file_path)
        except FileNotFoundError:
            pass

    def setUp(self):
        """Clear the storage before each test"""
        self.storage._FileStorage__objects = {}  # Clear the storage
        self.model = BaseModel()  # Create a model instance for testing

    def test_new(self):
        """Test that new adds an object to the storage"""
        self.storage.new(self.model)
        self.storage.save()
        all_objs = self.storage.all()
        self.assertEqual(len(all_objs), 1)

    def test_reload(self):
        """Test that reload properly loads objects from the file"""
        self.storage.new(self.model)
        self.storage.save()
        # Clear and reload storage
        self.storage._FileStorage__objects = {}  # Clear the storage
        self.storage.reload()
        all_objs = self.storage.all()
        self.assertEqual(len(all_objs), 1)

    def test_save(self):
        """Test that save properly saves objects to the file"""
        model2 = BaseModel()
        self.storage.new(self.model)
        self.storage.new(model2)
        self.storage.save()
        self.storage._FileStorage__objects = {}  # Clear the storage
        self.storage.reload()
        all_objs = self.storage.all()
        self.assertEqual(len(all_objs), 2)

    def test_save_reload_new_instance(self):
        """Test saving and reloading with a new instance"""
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.storage.new(obj1)
        self.storage.new(obj2)
        self.storage.save()
        self.storage._FileStorage__objects = {}  # Clear the storage
        self.storage.reload()
        all_objs = self.storage.all()
        self.assertEqual(len(all_objs), 2)

if __name__ == "__main__":
    unittest.main()
