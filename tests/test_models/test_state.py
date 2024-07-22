#!/usr/bin/python3

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
import unittest
from models.state import State

class TestState(unittest.TestCase):

    def setUp(self):
        self.state = State()

    def test_state_inherits_base_model(self):
        from models.base_model import BaseModel
        self.assertIsInstance(self.state, BaseModel)

    def test_state_has_name_attribute(self):
        self.assertTrue(hasattr(self.state, 'name'))
        self.assertEqual(self.state.name, "")

    def test_state_name_is_string(self):
        self.assertIsInstance(self.state.name, str)

    def test_state_to_dict_includes_state_attributes(self):
        state_dict = self.state.to_dict()
        self.assertIn('name', state_dict)

    def test_state_creation_with_kwargs(self):
        state_data = {
            'id': '123456',
            'created_at': '2024-07-22T14:22:18.182905',
            'updated_at': '2024-07-22T14:22:18.182915',
            'name': 'California'
        }
        state = State(**state_data)
        self.assertEqual(state.id, '123456')
        self.assertEqual(state.created_at.isoformat(), '2024-07-22T14:22:18.182905')
        self.assertEqual(state.updated_at.isoformat(), '2024-07-22T14:22:18.182915')
        self.assertEqual(state.name, 'California')

if __name__ == '__main__':
    unittest.main()
