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
