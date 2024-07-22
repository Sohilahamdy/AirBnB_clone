#!/usr/bin/python3

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
import unittest
from models.user import User

class TestUser(unittest.TestCase):

    def setUp(self):
        self.user = User()

    def test_user_inherits_base_model(self):
        from models.base_model import BaseModel
        self.assertIsInstance(self.user, BaseModel)

    def test_user_has_email_attribute(self):
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertEqual(self.user.email, "")

    def test_user_has_password_attribute(self):
        self.assertTrue(hasattr(self.user, 'password'))
        self.assertEqual(self.user.password, "")

    def test_user_has_first_name_attribute(self):
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertEqual(self.user.first_name, "")

    def test_user_has_last_name_attribute(self):
        self.assertTrue(hasattr(self.user, 'last_name'))
        self.assertEqual(self.user.last_name, "")

    def test_user_email_is_string(self):
        self.assertIsInstance(self.user.email, str)

    def test_user_password_is_string(self):
        self.assertIsInstance(self.user.password, str)

    def test_user_first_name_is_string(self):
        self.assertIsInstance(self.user.first_name, str)

    def test_user_last_name_is_string(self):
        self.assertIsInstance(self.user.last_name, str)

    def test_user_to_dict_includes_user_attributes(self):
        user_dict = self.user.to_dict()
        self.assertIn('email', user_dict)
        self.assertIn('password', user_dict)
        self.assertIn('first_name', user_dict)
        self.assertIn('last_name', user_dict)

    def test_user_creation_with_kwargs(self):
        user_data = {
            'id': '123456',
            'created_at': '2024-07-22T14:22:18.182905',
            'updated_at': '2024-07-22T14:22:18.182915',
            'email': 'test@example.com',
            'password': '1234',
            'first_name': 'John',
            'last_name': 'Doe'
        }
        user = User(**user_data)
        self.assertEqual(user.id, '123456')
        self.assertEqual(user.created_at.isoformat(), '2024-07-22T14:22:18.182905')
        self.assertEqual(user.updated_at.isoformat(), '2024-07-22T14:22:18.182915')
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.password, '1234')
        self.assertEqual(user.first_name, 'John')
        self.assertEqual(user.last_name, 'Doe')

if __name__ == '__main__':
    unittest.main()
