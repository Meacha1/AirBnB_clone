#!/usr/bin/python3
""" Class Review that inherits from base model"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Class for the Review model

    Attributes:
        place_id (str): empty string for the id of the place
        user_id (str): empty string for the id of the user
        text (str): empty string for the review text
    """
    place_id = ""
    user_id = ""
    text = ""
