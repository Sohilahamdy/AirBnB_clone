#!/usr/bin/python3
import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class"""

    def setUp(self):
        """Set up test environment"""
        self.model = BaseModel()
        self.model.name = "Test Model"
        self.model.number = 42

    def test_instance(self):
        """Test that BaseModel is an instance of BaseModel"""
        self.assertIsInstance(self.model, BaseModel)

    def test_kwargs(self):
        """Test creation of instance with kwargs"""
        model_dict = self.model.to_dict()
        new_model = BaseModel(**model_dict)
        self.assertEqual(self.model.id, new_model.id)
        self.assertEqual(self.model.created_at, new_model.created_at)
        self.assertEqual(self.model.updated_at, new_model.updated_at)
        self.assertEqual(self.model.name, new_model.name)
        self.assertEqual(self.model.number, new_model.number)

    def test_save(self):
        """Test the save method"""
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at, self.model.created_at)

    def test_to_dict(self):
        """Test that to_dict method creates accurate dictionary."""
        model_dict = self.model.to_dict()
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['name'], 'Test Model')
        self.assertEqual(model_dict['number'], 42)
        self.assertEqual(model_dict['id'], self.model.id)
        self.assertIn("created_at", model_dict)
        self.assertIn("updated_at", model_dict)

if __name__ == '__main__':
    unittest.main()
