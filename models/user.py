#!/usr/bin/python3
""" Class user that inherits from base model"""

from models.base_model import BaseModel


# Define the class User that inherits from BaseModel
class User(BaseModel):
    # Define the public class attributes for User
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    # Document the constructor method for User
    def __init__(self, *args, **kwargs):
        """
        Initializes a new User instance
        """
        # Call the parent constructor method to initialize the BaseModel attributes
        super().__init__(*args, **kwargs)
