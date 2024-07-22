#!/usr/bin/python3

import unittest
import os
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class"""

    def setUp(self):
        """Set up test environment"""
        self.storage = FileStorage()
        self.model = BaseModel()
        self.storage.new(self.model)
        self.file_path = self.storage._FileStorage__file_path

    def tearDown(self):
        """Clean up after tests"""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        del self.storage
        del self.model

    def test_all(self):
        """Test that all returns the dictionary of objects"""
        all_objs = self.storage.all()
        self.assertEqual(len(all_objs), 1)
        self.assertIn(f'BaseModel.{self.model.id}', all_objs)

    def test_new(self):
        """Test that new adds an object to the storage"""
        new_model = BaseModel()
        self.storage.new(new_model)
        all_objs = self.storage.all()
        self.assertEqual(len(all_objs), 2)
        self.assertIn(f'BaseModel.{new_model.id}', all_objs)

    def test_save(self):
        """Test that save properly saves objects to the file"""
        self.storage.save()
        self.assertTrue(os.path.exists(self.file_path))
        with open(self.file_path, 'r') as f:
            data = json.load(f)
            self.assertIn(f'BaseModel.{self.model.id}', data)

    def test_reload(self):
        """Test that reload properly loads objects from the file"""
        self.storage.save()
        self.storage.reload()
        all_objs = self.storage.all()
        self.assertEqual(len(all_objs), 1)
        self.assertIn(f'BaseModel.{self.model.id}', all_objs)
        loaded_model = all_objs[f'BaseModel.{self.model.id}']
        self.assertEqual(loaded_model.id, self.model.id)
        self.assertEqual(loaded_model.created_at.isoformat(), self.model.created_at.isoformat())
        self.assertEqual(loaded_model.updated_at.isoformat(), self.model.updated_at.isoformat())

    def test_save_reload_new_instance(self):
        """Test saving and reloading with a new instance"""
        self.storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        all_objs = new_storage.all()
        self.assertEqual(len(all_objs), 1)
        self.assertIn(f'BaseModel.{self.model.id}', all_objs)

if __name__ == '__main__':
    unittest.main()
