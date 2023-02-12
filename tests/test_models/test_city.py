#!/usr/bin/python3
import unittest
from models.city import City
from models.base_model import BaseModel

class TestCity(unittest.TestCase):
    """
    Unittest for the City class.
    """
    def setUp(self):
        """
        Set up method to run before each test cases.
        """
        self.city = City()

    def tearDown(self):
        """
        Tear down method to run after each test cases.
        """
        del self.city

    def test_instance(self):
        """
        Test the creation of an instance of City.
        """
        self.assertIsInstance(self.city, City)
        self.assertIsInstance(self.city, BaseModel)

    def test_attributes(self):
        """
        Test the existence of attributes and its types.
        """
        self.assertTrue(hasattr(self.city, "state_id"))
        self.assertTrue(hasattr(self.city, "name"))
        self.assertEqual(type(self.city.state_id), str)
        self.assertEqual(type(self.city.name), str)

    def test_default_attributes(self):
        """
        Test the default values of attributes.
        """
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")

    def test_saving(self):
        """
        Test if the object is correctly saved in the JSON file.
        """
        self.city.save()
        self.assertNotEqual(self.city.created_at, self.city.updated_at)

if __name__ == "__main__":
    unittest.main()
