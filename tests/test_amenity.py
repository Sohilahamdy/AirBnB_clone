#!/usr/bin/python3

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel

class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class"""

    def setUp(self):
        """Set up test environment"""
        self.amenity = Amenity()
        self.amenity.name = "Pool"
    
    def test_instance(self):
        """Test that Amenity is an instance of BaseModel and Amenity"""
        self.assertIsInstance(self.amenity, BaseModel)
        self.assertIsInstance(self.amenity, Amenity)
    
    def test_attributes(self):
        """Test that Amenity has the correct attributes"""
        self.assertTrue(hasattr(self.amenity, "name"))
        self.assertEqual(self.amenity.name, "Pool")

    def test_to_dict(self):
        """Test the to_dict method of Amenity"""
        amenity_dict = self.amenity.to_dict()
        self.assertEqual(type(amenity_dict), dict)
        self.assertIn('__class__', amenity_dict)
        self.assertEqual(amenity_dict['__class__'], 'Amenity')
        self.assertIn('name', amenity_dict)
        self.assertEqual(amenity_dict['name'], 'Pool')
        self.assertIn('id', amenity_dict)
        self.assertIn('created_at', amenity_dict)
        self.assertIn('updated_at', amenity_dict)

    def test_str_method(self):
        """Test the __str__ method of Amenity"""
        string_rep = str(self.amenity)
        self.assertIn("[Amenity]", string_rep)
        self.assertIn("({})".format(self.amenity.id), string_rep)
        self.assertIn("name: Pool", string_rep)

if __name__ == '__main__':
    unittest.main()
