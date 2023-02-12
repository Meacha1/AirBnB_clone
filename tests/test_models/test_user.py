#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.user import User

class TestUser(unittest.TestCase):
    """Class for testing the User class."""

    def setUp(self):
        """Set up method that runs before each test."""
        self.user = User()
    
    def tearDown(self):
        """Tear down method that runs after each test."""
        del self.user

    def test_is_base_model(self):
        """Test if User is a subclass of BaseModel."""
        self.assertIsInstance(self.user, BaseModel)
    
    def test_email(self):
        """Test if the email attribute is a string and if it's empty by default."""
        self.assertIsInstance(self.user.email, str)
        self.assertEqual(self.user.email, "")

    def test_password(self):
        """Test if the password attribute is a string and if it's empty by default."""
        self.assertIsInstance(self.user.password, str)
        self.assertEqual(self.user.password, "")
    
    def test_first_name(self):
        """Test if the first_name attribute is a string and if it's empty by default."""
        self.assertIsInstance(self.user.first_name, str)
        self.assertEqual(self.user.first_name, "")

    def test_last_name(self):
        """Test if the last_name attribute is a string and if it's empty by default."""
        self.assertIsInstance(self.user.last_name, str)
        self.assertEqual(self.user.last_name, "")

if __name__ == '__main__':
    unittest.main()
