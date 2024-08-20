#!/usr/bin/python3

import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.file_path = 'file.json'

    @classmethod
    def tearDownClass(cls):
        try:
            os.remove(cls.file_path)
        except FileNotFoundError:
            pass

    def setUp(self):
        self.storage = FileStorage()
        self.storage._FileStorage__file_path = self.file_path
        self.storage._FileStorage__objects = {}
        self.model = BaseModel()
        self.storage.new(self.model)
        self.storage.save()

    def tearDown(self):
        """Teardown for each test"""
        try:
            os.remove(self.file_path)
        except FileNotFoundError:
            pass

    def test_new(self):
        """Test that new adds an object to storage"""
        new_model = BaseModel()
        self.storage.new(new_model)
        self.storage.save()
        all_objs = self.storage.all()
        self.assertEqual(len(all_objs), 2)

    def test_reload(self):
        """Test that reload properly loads objects from the file"""
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
        self.assertTrue(os.path.exists(self.file_path))
        with open(self.file_path, 'r') as f:
            data = f.read()
        self.assertGreater(len(data), 0)
        self.storage._FileStorage__objects = {}  # Clear storage
        self.storage.reload()
        all_objs = self.storage.all()
        self.assertEqual(len(all_objs), 2)
        self.assertTrue(any(obj.id == self.model.id for obj in all_objs.values()))
        self.assertTrue(any(obj.id == model2.id for obj in all_objs.values()))

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
        self.assertEqual(len(all_objs), 3)

    def test_objects(self):
        """Test that __objects is properly updated"""
        key = f"{self.model.__class__.__name__}.{self.model.id}"
        self.assertIn(key, self.storage.all())

    def test_objects_internal(self):
        """Test that __objects internal state is properly managed"""
        all_objs = self.storage.all()
        self.assertTrue(hasattr(self.storage, '_FileStorage__objects'))
        self.assertEqual(type(self.storage._FileStorage__objects), dict)
        self.assertGreater(len(self.storage._FileStorage__objects), 0)
        self.assertEqual(len(all_objs), 1)

    def print_all_objs(self, message=""):
        """Print all objects in storage with an optional message"""
        print(message)
        for key, obj in self.storage.all().items():
            print(f"{key}: {obj.to_dict()}")

if __name__ == "__main__":
    unittest.main()
