#!/usr/bin/python3
""" Class place that inherits from base model"""

from models.base_model import BaseModel


class Place(BaseModel):
    """Class for the Place model

    Attributes:
        city_id (str): empty string for the id of the city
        user_id (str): empty string for the id of the user
        name (str): empty string for the name of the place
        description (str): empty string for the description of the place
        number_rooms (int): 0 for the number of rooms in the place
        number_bathrooms (int): 0 for the number of bathrooms in the place
        max_guest (int): 0 for the maximum number of guests allowed
        price_by_night (int): 0 for the price per night
        latitude (float): 0.0 for the latitude coordinate
        longitude (float): 0.0 for the longitude coordinate
        amenity_ids (list of str): empty list for the ids of amenities
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
