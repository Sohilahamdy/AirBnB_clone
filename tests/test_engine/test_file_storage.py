#!/usr/bin/python3
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class."""

    @classmethod
    def setUpClass(cls):
        """Set up the test class environment."""
        cls.storage = FileStorage()
        cls.storage.reload()

    def setUp(self):
        """Set up the test environment."""
        self.storage.reload()
        self.model = BaseModel()
        self.storage.new(self.model)
        self.storage.save()

    def tearDown(self):
        """Clean up after each test."""
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_all(self):
        """Test the all() method."""
        all_objects = self.storage.all()
        self.assertIsInstance(all_objects, dict)
        self.assertIn(f"BaseModel.{self.model.id}", all_objects)

    def test_new(self):
        """Test the new() method."""
        new_model = BaseModel()
        self.storage.new(new_model)
        self.assertIn(f"BaseModel.{new_model.id}", self.storage.all())

    def test_save(self):
        """Test the save() method."""
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()
        self.storage.reload()
        self.assertIn(f"BaseModel.{model.id}", self.storage.all())

    def test_get(self):
        """Test the get() method."""
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()
        self.storage.reload()
        retrieved_model = self.storage.get(BaseModel, model.id)
        self.assertEqual(retrieved_model.id, model.id)

    def test_get_method(self):
        """Test that get() method retrieves an object by ID."""
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()
        retrieved_model = self.storage.get(BaseModel, model.id)
        self.assertEqual(retrieved_model, model)

    def test_delete(self):
        """Test the delete() method."""
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()
        self.storage.delete(model)
        self.storage.save()
        self.storage.reload()
        self.assertNotIn(f"BaseModel.{model.id}", self.storage.all())

    def test_update(self):
        """Test the update() method."""
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()
        model.name = "Updated Name"
        self.storage.save()
        self.storage.reload()
        updated_model = self.storage.all().get(f"BaseModel.{model.id}")
        self.assertEqual(updated_model.name, "Updated Name")

    def test_reload(self):
        """Test the reload() method."""
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()
        self.storage.reload()
        all_objects = self.storage.all()
        self.assertIn(f"BaseModel.{model.id}", all_objects)

if __name__ == '__main__':
    unittest.main()
