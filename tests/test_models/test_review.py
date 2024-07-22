#!/usr/bin/python3

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
import unittest
from models.review import Review

class TestReview(unittest.TestCase):

    def setUp(self):
        self.review = Review()

    def test_review_inherits_base_model(self):
        from models.base_model import BaseModel
        self.assertIsInstance(self.review, BaseModel)

    def test_review_has_place_id_attribute(self):
        self.assertTrue(hasattr(self.review, 'place_id'))
        self.assertEqual(self.review.place_id, "")

    def test_review_has_user_id_attribute(self):
        self.assertTrue(hasattr(self.review, 'user_id'))
        self.assertEqual(self.review.user_id, "")

    def test_review_has_text_attribute(self):
        self.assertTrue(hasattr(self.review, 'text'))
        self.assertEqual(self.review.text, "")

    def test_review_place_id_is_string(self):
        self.assertIsInstance(self.review.place_id, str)

    def test_review_user_id_is_string(self):
        self.assertIsInstance(self.review.user_id, str)

    def test_review_text_is_string(self):
        self.assertIsInstance(self.review.text, str)

    def test_review_to_dict_includes_review_attributes(self):
        review_dict = self.review.to_dict()
        self.assertIn('place_id', review_dict)
        self.assertIn('user_id', review_dict)
        self.assertIn('text', review_dict)

    def test_review_creation_with_kwargs(self):
        review_data = {
            'id': '345678',
            'created_at': '2024-07-22T14:22:18.182905',
            'updated_at': '2024-07-22T14:22:18.182915',
            'place_id': 'place_123',
            'user_id': 'user_456',
            'text': 'Great place!'
        }
        review = Review(**review_data)
        self.assertEqual(review.id, '345678')
        self.assertEqual(review.created_at.isoformat(), '2024-07-22T14:22:18.182905')
        self.assertEqual(review.updated_at.isoformat(), '2024-07-22T14:22:18.182915')
        self.assertEqual(review.place_id, 'place_123')
        self.assertEqual(review.user_id, 'user_456')
        self.assertEqual(review.text, 'Great place!')

if __name__ == '__main__':
    unittest.main()
