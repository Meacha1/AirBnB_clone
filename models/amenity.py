#!/usr/bin/python3
""" Class amenity that inherits from base model"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Class for the Amenity model

    Attributes:
        name (str): empty string for the name of the amenity
    """
    name = ""
