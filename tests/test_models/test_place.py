#!/usr/bin/python3
import unittest
from models.amenity import Amenity
import pep8

class TestAmenity(unittest.TestCase):
    """Class to test the Amenity class"""

    def setUp(self):
        """Method to create an instance of Amenity before each test"""
        self.amenity = Amenity()

    def tearDown(self):
        """Method to delete the instance of Amenity after each test"""
        del self.amenity

    def test_has_attribute_name(self):
        """Tests if the Amenity class has the name attribute"""
        self.assertTrue(hasattr(self.amenity, "name"))

    def test_has_attribute_id(self):
        """Tests if the Amenity class has the id attribute"""
        self.assertTrue(hasattr(self.amenity, "id"))

    def test_has_attribute_created_at(self):
        """Tests if the Amenity class has the created_at attribute"""
        self.assertTrue(hasattr(self.amenity, "created_at"))

    def test_created_at_attribute_datetime(self):
        """Tests if the created_at attribute is a datetime object"""
        from datetime import datetime
        self.assertIsInstance(self.amenity.created_at, datetime)

    def test_has_attribute_updated_at(self):
        """Tests if the Amenity class has the updated_at attribute"""
        self.assertTrue(hasattr(self.amenity, "updated_at"))

    def test_updated_at_attribute_datetime(self):
        """Tests if the updated_at attribute is a datetime object"""
        from datetime import datetime
        self.assertIsInstance(self.amenity.updated_at, datetime)

    def test_pep8_conformance(self):
        """Tests if the code follows PEP8 style guide"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

if __name__ == "__main__":
    unittest.main()
