#!/usr/bin/python3
# models/user.py
from models.base_model import BaseModel

class User(BaseModel):
    """Represent a User in the AirBnB system."""

    def __init__(self, email="", password="", first_name="", last_name="", *args, **kwargs):
        """Initialize a User instance.

        Args:
            email (str): The user's email address.
            password (str): The user's password.
            first_name (str): The user's first name.
            last_name (str): The user's last name.
        """
        super().__init__(*args, **kwargs)
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        """Return a string representation of the User instance."""
        return "[User] ({}) {}".format(self.id, self.__dict__)

    def full_name(self):
        """Return the full name of the user."""
        return "{} {}".format(self.first_name, self.last_name)
