#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
import pep8

class TestBaseModel(unittest.TestCase):
    """This class will test the BaseModel class"""

    def setUp(self):
        """This method will run before each test, it will create a new instance of the BaseModel class"""
        self.base_model = BaseModel()

    def test_pep8_conformance(self):
        """Test that we conform to PEP8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_instantiation(self):
        """This method will test if the instance of BaseModel is well created"""
        self.assertIsInstance(self.base_model, BaseModel)

    def test_has_attribute_id(self):
        """This method will check if the instance has the id attribute"""
        self.assertTrue(hasattr(self.base_model, "id"))

    def test_has_attribute_created_at(self):
        """This method will check if the instance has the created_at attribute"""
        self.assertTrue(hasattr(self.base_model, "created_at"))

    def test_has_attribute_updated_at(self):
        """This method will check if the instance has the updated_at attribute"""
        self.assertTrue(hasattr(self.base_model, "updated_at"))

    def test_type_id(self):
        """This method will check the type of the id attribute"""
        self.assertEqual(type(self.base_model.id), str)

    def test_type_created_at(self):
        """This method will check the type of the created_at attribute"""
        self.assertEqual(type(self.base_model.created_at), str)

    def test_type_updated_at(self):
        """This method will check the type of the updated_at attribute"""
        self.assertEqual(type(self.base_model.updated_at), str)

if __name__ == '__main__':
    unittest.main()
