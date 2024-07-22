#!/usr/bin/python3

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
import unittest
from models.place import Place

class TestPlace(unittest.TestCase):

    def setUp(self):
        self.place = Place()

    def test_place_inherits_base_model(self):
        from models.base_model import BaseModel
        self.assertIsInstance(self.place, BaseModel)

    def test_place_has_city_id_attribute(self):
        self.assertTrue(hasattr(self.place, 'city_id'))
        self.assertEqual(self.place.city_id, "")

    def test_place_has_user_id_attribute(self):
        self.assertTrue(hasattr(self.place, 'user_id'))
        self.assertEqual(self.place.user_id, "")

    def test_place_has_name_attribute(self):
        self.assertTrue(hasattr(self.place, 'name'))
        self.assertEqual(self.place.name, "")

    def test_place_has_description_attribute(self):
        self.assertTrue(hasattr(self.place, 'description'))
        self.assertEqual(self.place.description, "")

    def test_place_has_number_rooms_attribute(self):
        self.assertTrue(hasattr(self.place, 'number_rooms'))
        self.assertEqual(self.place.number_rooms, 0)

    def test_place_has_number_bathrooms_attribute(self):
        self.assertTrue(hasattr(self.place, 'number_bathrooms'))
        self.assertEqual(self.place.number_bathrooms, 0)

    def test_place_has_max_guest_attribute(self):
        self.assertTrue(hasattr(self.place, 'max_guest'))
        self.assertEqual(self.place.max_guest, 0)

    def test_place_has_price_by_night_attribute(self):
        self.assertTrue(hasattr(self.place, 'price_by_night'))
        self.assertEqual(self.place.price_by_night, 0)

    def test_place_has_latitude_attribute(self):
        self.assertTrue(hasattr(self.place, 'latitude'))
        self.assertEqual(self.place.latitude, 0.0)

    def test_place_has_longitude_attribute(self):
        self.assertTrue(hasattr(self.place, 'longitude'))
        self.assertEqual(self.place.longitude, 0.0)

    def test_place_has_amenity_ids_attribute(self):
        self.assertTrue(hasattr(self.place, 'amenity_ids'))
        self.assertIsInstance(self.place.amenity_ids, list)
        self.assertEqual(self.place.amenity_ids, [])

    def test_place_city_id_is_string(self):
        self.assertIsInstance(self.place.city_id, str)

    def test_place_user_id_is_string(self):
        self.assertIsInstance(self.place.user_id, str)

    def test_place_name_is_string(self):
        self.assertIsInstance(self.place.name, str)

    def test_place_description_is_string(self):
        self.assertIsInstance(self.place.description, str)

    def test_place_number_rooms_is_integer(self):
        self.assertIsInstance(self.place.number_rooms, int)

    def test_place_number_bathrooms_is_integer(self):
        self.assertIsInstance(self.place.number_bathrooms, int)

    def test_place_max_guest_is_integer(self):
        self.assertIsInstance(self.place.max_guest, int)

    def test_place_price_by_night_is_integer(self):
        self.assertIsInstance(self.place.price_by_night, int)

    def test_place_latitude_is_float(self):
        self.assertIsInstance(self.place.latitude, float)

    def test_place_longitude_is_float(self):
        self.assertIsInstance(self.place.longitude, float)

    def test_place_to_dict_includes_place_attributes(self):
        place_dict = self.place.to_dict()
        self.assertIn('city_id', place_dict)
        self.assertIn('user_id', place_dict)
        self.assertIn('name', place_dict)
        self.assertIn('description', place_dict)
        self.assertIn('number_rooms', place_dict)
        self.assertIn('number_bathrooms', place_dict)
        self.assertIn('max_guest', place_dict)
        self.assertIn('price_by_night', place_dict)
        self.assertIn('latitude', place_dict)
        self.assertIn('longitude', place_dict)
        self.assertIn('amenity_ids', place_dict)

    def test_place_creation_with_kwargs(self):
        place_data = {
            'id': '123456',
            'created_at': '2024-07-22T14:22:18.182905',
            'updated_at': '2024-07-22T14:22:18.182915',
            'city_id': 'city_123',
            'user_id': 'user_123',
            'name': 'My Place',
            'description': 'A lovely place',
            'number_rooms': 3,
            'number_bathrooms': 2,
            'max_guest': 4,
            'price_by_night': 150,
            'latitude': 37.7749,
            'longitude': -122.4194,
            'amenity_ids': ['amenity_1', 'amenity_2']
        }
        place = Place(**place_data)
        self.assertEqual(place.id, '123456')
        self.assertEqual(place.created_at.isoformat(), '2024-07-22T14:22:18.182905')
        self.assertEqual(place.updated_at.isoformat(), '2024-07-22T14:22:18.182915')
        self.assertEqual(place.city_id, 'city_123')
        self.assertEqual(place.user_id, 'user_123')
        self.assertEqual(place.name, 'My Place')
        self.assertEqual(place.description, 'A lovely place')
        self.assertEqual(place.number_rooms, 3)
        self.assertEqual(place.number_bathrooms, 2)
        self.assertEqual(place.max_guest, 4)
        self.assertEqual(place.price_by_night, 150)
        self.assertEqual(place.latitude, 37.7749)
        self.assertEqual(place.longitude, -122.4194)
        self.assertEqual(place.amenity_ids, ['amenity_1', 'amenity_2'])

if __name__ == '__main__':
    unittest.main()
