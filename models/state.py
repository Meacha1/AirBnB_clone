#!/usr/bin/python3
""" Class state that inherits from base model"""

from models.base_model import BaseModel


class State(BaseModel):
    """Class for the State model

    Attributes:
        name (str): empty string for the name of the state
    """
    name = ""
