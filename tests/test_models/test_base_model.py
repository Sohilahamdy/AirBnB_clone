# tests/test_models/test_base_model.py
import unittest
from models.base_model import BaseModel
import datetime
import uuid

class TestBaseModel(unittest.TestCase):

    def setUp(self):
        """Set up a test case with a new instance of BaseModel."""
        self.model = BaseModel()

    def test_id_is_uuid(self):
        """Test if id is a valid UUID."""
        self.assertIsInstance(uuid.UUID(self.model.id), uuid.UUID)

    def test_created_at_is_datetime(self):
        """Test if created_at is a datetime object."""
        self.assertIsInstance(self.model.created_at, datetime.datetime)

    def test_updated_at_is_datetime(self):
        """Test if updated_at is a datetime object."""
        self.assertIsInstance(self.model.updated_at, datetime.datetime)

    def test_save_updates_updated_at(self):
        """Test if save method updates updated_at attribute."""
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)

    def test_to_dict(self):
        """Test if to_dict method returns a dictionary."""
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['id'], self.model.id)
        self.assertEqual(model_dict['created_at'], self.model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], self.model.updated_at.isoformat())
        self.assertEqual(model_dict['__class__'], 'BaseModel')

if __name__ == '__main__':
    unittest.main()

