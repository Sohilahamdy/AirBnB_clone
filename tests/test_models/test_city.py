#!/usr/bin/python3

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
import unittest
from models.city import City

class TestCity(unittest.TestCase):

    def setUp(self):
        self.city = City()

    def test_city_inherits_base_model(self):
        from models.base_model import BaseModel
        self.assertIsInstance(self.city, BaseModel)

    def test_city_has_name_attribute(self):
        self.assertTrue(hasattr(self.city, 'name'))
        self.assertEqual(self.city.name, "")

    def test_city_has_state_id_attribute(self):
        self.assertTrue(hasattr(self.city, 'state_id'))
        self.assertEqual(self.city.state_id, "")

    def test_city_name_is_string(self):
        self.assertIsInstance(self.city.name, str)

    def test_city_state_id_is_string(self):
        self.assertIsInstance(self.city.state_id, str)

    def test_city_to_dict_includes_city_attributes(self):
        city_dict = self.city.to_dict()
        self.assertIn('name', city_dict)
        self.assertIn('state_id', city_dict)

    def test_city_creation_with_kwargs(self):
        city_data = {
            'id': '654321',
            'created_at': '2024-07-22T14:22:18.182905',
            'updated_at': '2024-07-22T14:22:18.182915',
            'name': 'San Francisco',
            'state_id': 'CA'
        }
        city = City(**city_data)
        self.assertEqual(city.id, '654321')
        self.assertEqual(city.created_at.isoformat(), '2024-07-22T14:22:18.182905')
        self.assertEqual(city.updated_at.isoformat(), '2024-07-22T14:22:18.182915')
        self.assertEqual(city.name, 'San Francisco')
        self.assertEqual(city.state_id, 'CA')

if __name__ == '__main__':
    unittest.main()
