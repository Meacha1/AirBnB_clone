#!/usr/bin/python3
import unittest
from models.state import State
import pep8

class TestState(unittest.TestCase):
    '''This class tests the State class'''

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_new_state(self):
        '''Test to create a new State'''
        s1 = State()
        self.assertEqual(s1.name, '')

    def test_to_dict_state(self):
        '''Test to dictionary representation of State'''
        s1 = State()
        s1.name = "California"
        s1_dict = s1.to_dict()
        self.assertEqual(s1_dict['name'], "California")
        self.assertTrue(type(s1_dict['created_at']) is str)
        self.assertTrue(type(s1_dict['updated_at']) is str)

    def test_str_method(self):
        '''Test the string representation of State'''
        s1 = State()
        s1.name = "California"
        s1_str = str(s1)
        self.assertEqual(s1_str, "[State] (0000-00-00 00:00:00) California")

if __name__ == '__main__':
    unittest.main()
