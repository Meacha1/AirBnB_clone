#!/usr/bin/python3
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel

class TestAmenity(unittest.TestCase):
    """Tests for the Amenity class"""

    def test_inheritance(self):
        """Tests if Amenity inherits from BaseModel"""
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)

    def test_attributes(self):
        """Tests if Amenity has the correct attributes"""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")
        self.assertEqual(amenity.id, "")
        self.assertEqual(amenity.created_at, "")
        self.assertEqual(amenity.updated_at, "")

    def test_attribute_assignment(self):
        """Tests if the attributes can be assigned correctly"""
        amenity = Amenity()
        amenity.name = "Pool"
        self.assertEqual(amenity.name, "Pool")

if __name__ == "__main__":
    unittest.main()
