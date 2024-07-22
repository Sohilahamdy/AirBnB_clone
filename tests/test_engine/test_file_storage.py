#!/usr/bin/python3
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):

    def setUp(self):
        """Set up for FileStorage tests."""
        self.storage = FileStorage()
        self.storage._FileStorage__objects = {}
        self.storage_file = 'file.json'
        if os.path.exists(self.storage_file):
            os.remove(self.storage_file)

    def tearDown(self):
        """Clean up after tests."""
        if os.path.exists(self.storage_file):
            os.remove(self.storage_file)

    def test_all_returns_dict(self):
        """Test that all() method returns a dictionary."""
        self.assertIsInstance(self.storage.all(), dict)

    def test_new_adds_object(self):
        """Test that new() method adds an object to the storage."""
        model = BaseModel()
        self.storage.new(model)
        key = f"{model.__class__.__name__}.{model.id}"
        self.assertIn(key, self.storage.all())

    def test_save_creates_file(self):
        """Test that save() method creates a file."""
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()
        self.assertTrue(os.path.exists(self.storage_file))

    def test_reload_loads_objects(self):
        """Test that reload() method loads objects from the file."""
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()
        self.storage._FileStorage__objects = {}
        self.storage.reload()
        key = f"{model.__class__.__name__}.{model.id}"
        self.assertIn(key, self.storage.all())

    def test_delete_method(self):
        """Test that delete() method removes an object."""
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()
        key = f"{model.__class__.__name__}.{model.id}"
        self.storage.delete(model)
        self.assertNotIn(key, self.storage.all())

    def test_get_method(self):
        """Test that get() method retrieves an object by ID."""
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()
        retrieved_model = self.storage.get(BaseModel, model.id)
        self.assertEqual(retrieved_model, model)

if __name__ == '__main__':
    unittest.main()
