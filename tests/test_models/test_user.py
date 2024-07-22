# tests/test_models/test_user.py
import unittest
from models.user import User

class TestUser(unittest.TestCase):

    def setUp(self):
        """Set up a test case with a new instance of User."""
        self.user = User()

    def test_email_attribute(self):
        """Test if User has email attribute."""
        self.user.email = "user@example.com"
        self.assertEqual(self.user.email, "user@example.com")

    def test_password_attribute(self):
        """Test if User has password attribute."""
        self.user.password = "password"
        self.assertEqual(self.user.password, "password")

    def test_first_name_attribute(self):
        """Test if User has first_name attribute."""
        self.user.first_name = "John"
        self.assertEqual(self.user.first_name, "John")

    def test_last_name_attribute(self):
        """Test if User has last_name attribute."""
        self.user.last_name = "Doe"
        self.assertEqual(self.user.last_name, "Doe")

if __name__ == '__main__':
    unittest.main()

