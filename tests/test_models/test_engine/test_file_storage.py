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
        self.file_path = self.storage._FileStorage__file_path
        
        # Ensure the file does not exist at the beginning
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        # Double-check the file is deleted
        self.assertFalse(os.path.exists(self.file_path), "The storage file should be deleted in setUp.")
        
        # Ensure a clean slate
        self.storage._FileStorage__objects = {}
        self.storage.reload()

    def tearDown(self):
        """Clean up after tests"""
        # Ensure the file is removed after each test
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        # Double-check the file is deleted
        self.assertFalse(os.path.exists(self.file_path), "The storage file should be deleted in tearDown.")
        
        # Clear objects to ensure no data persistence
        self.storage._FileStorage__objects = {}

    def test_all(self):
        """Test that all returns the dictionary of objects"""
        obj = BaseModel()
        self.storage.new(obj)
        all_objs = self.storage.all()
        self.assertEqual(len(all_objs), 1)
        self.assertIn(f'BaseModel.{obj.id}', all_objs)

    def test_new(self):
        """Test that new adds an object to the storage"""
        obj = BaseModel()
        self.storage.new(obj)
        all_objs = self.storage.all()
        self.assertEqual(len(all_objs), 1)
        self.assertIn(f'BaseModel.{obj.id}', all_objs)

    def test_save(self):
        """Test that save properly saves objects to the file"""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.assertTrue(os.path.exists(self.file_path))
        with open(self.file_path, 'r') as f:
            data = json.load(f)
            self.assertIn(f'BaseModel.{obj.id}', data)

    def test_reload(self):
        """Test that reload properly loads objects from the file"""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.storage._FileStorage__objects = {}  # Clear the current objects
        self.storage.reload()
        all_objs = self.storage.all()
        self.assertEqual(len(all_objs), 1)
        self.assertIn(f'BaseModel.{obj.id}', all_objs)
        self.assertEqual(obj.id, all_objs[f'BaseModel.{obj.id}'].id)

    def test_save_reload_new_instance(self):
        """Test saving and reloading with a new instance"""
        # Create a new BaseModel instance and add it to storage
        obj = BaseModel()
        self.storage.new(obj)
        
        # Save the objects to file
        self.storage.save()
        
        # Clear the current objects in memory to simulate fresh start
        self.storage._FileStorage__objects = {}
        
        # Reload objects from the file
        self.storage.reload()
        
        # Retrieve all objects from storage
        all_objs = self.storage.all()
        
        # Check that there is exactly one object after reloading
        self.assertEqual(len(all_objs), 1)
        
        # Check that the reloaded object has the same ID as the original object
        self.assertIn(f'BaseModel.{obj.id}', all_objs)
        
        # Ensure the reloaded object is indeed the same as the original
        self.assertEqual(obj.id, all_objs[f'BaseModel.{obj.id}'].id)
        self.assertEqual(obj.created_at, all_objs[f'BaseModel.{obj.id}'].created_at)
        self.assertEqual(obj.updated_at, all_objs[f'BaseModel.{obj.id}'].updated_at)

if __name__ == '__main__':
    unittest.main()
