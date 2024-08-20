#!/usr/bin/python3
# models/place.py
from models.base_model import BaseModel

class Place(BaseModel):
    """Represent a Place in the AirBnB system."""

    def __init__(self, city_id="", user_id="", name="", description="", number_rooms=0,
                 number_bathrooms=0, max_guest=0, price_by_night=0, latitude=0.0,
                 longitude=0.0, amenity_ids=None, *args, **kwargs):
        """Initialize a Place instance.

        Args:
            city_id (str): The ID of the city where the place is located.
            user_id (str): The ID of the user who owns the place.
            name (str): The name of the place.
            description (str): A description of the place.
            number_rooms (int): The number of rooms in the place.
            number_bathrooms (int): The number of bathrooms in the place.
            max_guest (int): The maximum number of guests the place can accommodate.
            price_by_night (int): The price per night to stay at the place.
            latitude (float): The latitude of the place.
            longitude (float): The longitude of the place.
            amenity_ids (list): A list of IDs for amenities associated with the place.
        """
        super().__init__(*args, **kwargs)
        self.city_id = city_id
        self.user_id = user_id
        self.name = name
        self.description = description
        self.number_rooms = number_rooms
        self.number_bathrooms = number_bathrooms
        self.max_guest = max_guest
        self.price_by_night = price_by_night
        self.latitude = latitude
        self.longitude = longitude
        self.amenity_ids = amenity_ids if amenity_ids is not None else []

    def __str__(self):
        """Return a string representation of the Place instance."""
        return "[Place] ({}) {}".format(self.id, self.__dict__)

    @property
    def city(self):
        """Return the City instance to which this Place belongs.

        This method assumes there is a method to retrieve the city instance by ID.
        """
        from models import storage
        return storage.get("City", self.city_id)

    @property
    def user(self):
        """Return the User instance who owns this Place.

        This method assumes there is a method to retrieve the user instance by ID.
        """
        from models import storage
        return storage.get("User", self.user_id)

    @property
    def amenities(self):
        """Return a list of Amenity instances associated with this Place.

        This method assumes there is a method to retrieve amenities by their IDs.
        """
        from models import storage
        return [storage.get("Amenity", amenity_id) for amenity_id in self.amenity_ids]
