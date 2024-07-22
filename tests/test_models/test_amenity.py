#!/usr/bin/python3

import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):

    def setUp(self):
        self.amenity = Amenity()

    def test_amenity_inherits_base_model(self):
        from models.base_model import BaseModel
        self.assertIsInstance(self.amenity, BaseModel)

    def test_amenity_has_name_attribute(self):
        self.assertTrue(hasattr(self.amenity, 'name'))
        self.assertEqual(self.amenity.name, "")

    def test_amenity_name_is_string(self):
        self.assertIsInstance(self.amenity.name, str)

    def test_amenity_instance(self):
        """Test if Amenity instance is correctly created."""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)

    def test_amenity_to_dict_includes_amenity_attributes(self):
        amenity_dict = self.amenity.to_dict()
        self.assertIn('name', amenity_dict)

    def test_amenity_creation_with_kwargs(self):
        amenity_data = {
            'id': '789012',
            'created_at': '2024-07-22T14:22:18.182905',
            'updated_at': '2024-07-22T14:22:18.182915',
            'name': 'Pool'
        }
        amenity = Amenity(**amenity_data)
        self.assertEqual(amenity.id, '789012')
        self.assertEqual(amenity.created_at.isoformat(), '2024-07-22T14:22:18.182905')
        self.assertEqual(amenity.updated_at.isoformat(), '2024-07-22T14:22:18.182915')
        self.assertEqual(amenity.name, 'Pool')

if __name__ == '__main__':
    unittest.main()
