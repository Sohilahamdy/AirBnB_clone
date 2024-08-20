#!/usr/bin/python3
# models/city.py
from models.base_model import BaseModel

class City(BaseModel):
    """Represent a City in the AirBnB system."""

    def __init__(self, name="", state_id="", *args, **kwargs):
        """Initialize a City instance.

        Args:
            name (str): The name of the city.
            state_id (str): The ID of the state the city belongs to.
        """
        super().__init__(*args, **kwargs)
        self.name = name
        self.state_id = state_id

    def __str__(self):
        """Return a string representation of the City instance."""
        return "[City] ({}) {}".format(self.id, self.__dict__)

    @property
    def state(self):
        """Return the State instance to which this City belongs.

        This method assumes there is a method to retrieve the state instance by ID.
        """
        from models import storage
        return storage.get("State", self.state_id)
