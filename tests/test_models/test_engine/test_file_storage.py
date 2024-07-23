#!/usr/bin/python3

import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

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
        self.storage = FileStorage()
        self.storage._FileStorage__objects = {}
        self.model = BaseModel()
        self.storage.new(self.model)


    def test_new(self):
        """Test that new adds an object to storage"""
        new_model = BaseModel()
        self.storage.new(new_model)
        self.storage.save()
        
        self.print_all_objs("Contents of storage after adding new model in test_new:")
        
        all_objs = self.storage.all()
        self.assertEqual(len(all_objs), 1)

    def test_reload(self):
        """Test that reload properly loads objects from the file"""
        self.storage.new(self.model)
        self.storage.save()
        
        with open(self.file_path, 'r') as file:
            file_contents = file.read()
            print("Contents of file before reload:")
            print(file_contents)
        
        self.storage._FileStorage__objects = {}  # Clear storage
        self.storage.reload()
        all_objs = self.storage.all()

        with open(self.file_path, 'r') as file:
            file_contents = file.read()
            print("Contents of file after reload:")
            print(file_contents)

        self.assertEqual(len(all_objs), 1)

    def test_save(self):
        """Test that save properly saves objects to the file"""
        model2 = BaseModel()
        self.storage.new(self.model)
        self.storage.new(model2)
        self.storage.save()
        
        with open(self.file_path, 'r') as file:
            file_contents = file.read()
            print("Contents of file after save:")
            print(file_contents)
        
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
        
        self.print_all_objs("Contents of storage after save in test_save_reload_new_instance:")
        
        self.storage._FileStorage__objects = {}  # Clear storage
        self.storage.reload()
        
        all_objs = self.storage.all()
        
        self.print_all_objs("Contents of storage after reload in test_save_reload_new_instance:")
        
        self.assertEqual(len(all_objs), 2)

    def test_objects(self):
        """Test that __objects is properly updated"""
        key = f"{self.model.__class__.__name__}.{self.model.id}"
        self.assertIn(key, self.storage.all())

    def print_all_objs(self, message=""):
        """Print all objects in storage with an optional message"""
        print(message)
        for key, obj in self.storage.all().items():
            print(f"{key}: {obj.to_dict()}")

if __name__ == "__main__":
    unittest.main()
