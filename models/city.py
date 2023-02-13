#!/usr/bin/python3
""" Class city that inherits from base model"""

from models.base_model import BaseModel


class City(BaseModel):
    """Class for the City model

    Attributes:
        state_id (str): empty string for the id of the state
        name (str): empty string for the name of the city
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """ Constructor """
        super().__init__(self, *args, **kwargs)
