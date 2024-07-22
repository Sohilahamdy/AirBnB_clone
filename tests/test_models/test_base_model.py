#!/usr/bin/python3

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
import unittest
from models.base_model import BaseModel
import datetime
import uuid

class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.model = BaseModel()

    def test_id_is_uuid(self):
        self.assertIsInstance(uuid.UUID(self.model.id), uuid.UUID)

    def test_created_at_is_datetime(self):
        self.assertIsInstance(self.model.created_at, datetime.datetime)

    def test_updated_at_is_datetime(self):
        self.assertIsInstance(self.model.updated_at, datetime.datetime)

    def test_save_updates_updated_at(self):
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)

    def test_to_dict(self):
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['id'], self.model.id)
        self.assertEqual(model_dict['created_at'], self.model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], self.model.updated_at.isoformat())
        self.assertEqual(model_dict['__class__'], 'BaseModel')

if __name__ == '__main__':
    unittest.main()
