#!/usr/bin/python3

import uuid
import datetime
import models

class BaseModel:
    """
    BaseModel class that defines all common attributes/methods for other classes.

    Attributes:
        id (str): a string that is assigned a unique identifier (uuid) when an instance is created.
        created_at (datetime): the datetime when an instance is created.
        updated_at (datetime): the datetime when an instance is created and updated every time the object is changed.
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor of the BaseModel class.

        Args:
            *args: arguments that won't be used.
            **kwargs: a dictionary of key-value arguments where each key is an attribute name and each value is the value of this attribute.

        Returns:
            None
        """
        if kwargs:
            # For each key-value argument in kwargs, set the key as an attribute with the value as its value.
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    # If the key is created_at or updated_at, convert the string value to a datetime object.
                    setattr(self, key, datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != "__class__":
                    # If the key is not __class__, set the key as an attribute with the value as its value.
                    setattr(self, key, value)
        else:
            # If kwargs is empty, create a unique id and set created_at as the current datetime.
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.

        Returns:
            str: a string representation of the BaseModel instance.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the public instance attribute updated_at with the current datetime.

        Returns:
            None
        """
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary representation of the BaseModel instance.

        Returns:
            dict: a dictionary representation of the BaseModel instance.
        """
        dict_rep = self.__dict__.copy()
        dict_rep["__class__"] = self.__class__.__name__
        dict_rep["created_at"] = self.created_at.isoformat()
        dict_rep["updated_at"] = self.updated_at.isoformat()
        return dict_rep
