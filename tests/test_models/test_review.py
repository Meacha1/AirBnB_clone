#!/usr/bin/python3
import unittest
from models.review import Review
from models.base_model import BaseModel

class TestReview(unittest.TestCase):
    """
    TestReview class contains all the unit tests for the Review class
    """
    def setUp(self):
        """
        setUp method is called before each test
        Here, we create a new Review object to test
        """
        self.review = Review()

    def test_id_assignment(self):
        """
        This test case tests if the id of a review is being correctly assigned
        """
        review_id = "review_1"
        self.review.id = review_id
        self.assertEqual(self.review.id, review_id)

    def test_created_at_assignment(self):
        """
        This test case tests if the created_at attribute of a review is being correctly assigned
        """
        created_at = "2022-06-22T00:00:00.000000"
        self.review.created_at = created_at
        self.assertEqual(self.review.created_at, created_at)

    def test_updated_at_assignment(self):
        """
        This test case tests if the updated_at attribute of a review is being correctly assigned
        """
        updated_at = "2022-06-23T00:00:00.000000"
        self.review.updated_at = updated_at
        self.assertEqual(self.review.updated_at, updated_at)

    def test_place_id_assignment(self):
        """
        This test case tests if the place_id attribute of a review is being correctly assigned
        """
        place_id = "place_1"
        self.review.place_id = place_id
        self.assertEqual(self.review.place_id, place_id)

    def test_user_id_assignment(self):
        """
        This test case tests if the user_id attribute of a review is being correctly assigned
        """
        user_id = "user_1"
        self.review.user_id = user_id
        self.assertEqual(self.review.user_id, user_id)

    def test_text_assignment(self):
        """
        This test case tests if the text attribute of a review is being correctly assigned
        """
        text = "This is a great place!"
        self.review.text = text
        self.assertEqual(self.review.text, text)

if __name__ == "__main__":
    unittest.main()
