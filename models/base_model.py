#!/usr/bin/python3

import uuid
from datetime import datetime

class BaseModel:
    """
    Defines all common attributes and methods for other classes.
    """
    def __init__(self):
        """
        Initializes an instance of BaseModel.
        """
        # assign a unique id to each instance using uuid
        self.id = str(uuid.uuid4())
        # assign the current datetime when an instance is created
        self.created_at = datetime.now()
        # assign the current datetime when an instance is created and update every time the object changes
        self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the updated_at attribute with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary representation of the BaseModel instance.
        """
        # make a copy of the __dict__ attribute so that the original data remains unchanged
        dict_rep = self.__dict__.copy()
        # add a key "__class__" to the dictionary with the class name of the object
        dict_rep["__class__"] = self.__class__.__name__
        # convert the created_at and updated_at attributes to string in ISO format
        dict_rep["created_at"] = self.created_at.isoformat()
        dict_rep["updated_at"] = self.updated_at.isoformat()
        return dict_rep

