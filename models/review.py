#!/usr/bin/python3
# models/review.py
from models.base_model import BaseModel

class Review(BaseModel):
    """Represent a Review in the AirBnB system."""

    def __init__(self, place_id="", user_id="", text="", *args, **kwargs):
        """Initialize a Review instance.

        Args:
            place_id (str): The ID of the place being reviewed.
            user_id (str): The ID of the user who wrote the review.
            text (str): The content of the review.
        """
        super().__init__(*args, **kwargs)
        self.place_id = place_id
        self.user_id = user_id
        self.text = text

    def __str__(self):
        """Return a string representation of the Review instance."""
        return "[Review] ({}) {}".format(self.id, self.__dict__)

    @property
    def place(self):
        """Return the Place instance that this Review is associated with.

        This method assumes there is a method to retrieve the place instance by ID.
        """
        from models import storage
        return storage.get("Place", self.place_id)

    @property
    def user(self):
        """Return the User instance who wrote this Review.

        This method assumes there is a method to retrieve the user instance by ID.
        """
        from models import storage
        return storage.get("User", self.user_id)
