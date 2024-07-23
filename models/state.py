#!/usr/bin/python3
# models/state.py
from models.base_model import BaseModel

class State(BaseModel):
    """Represent a State in the AirBnB system."""

    def __init__(self, name="", *args, **kwargs):
        """Initialize a State instance.

        Args:
            name (str): The name of the state.
        """
        super().__init__(*args, **kwargs)
        self.name = name

    def __str__(self):
        """Return a string representation of the State instance."""
        return f"[State] ({self.id}) {self.__dict__}"

    def get_cities(self):
        """Return a list of City instances in this State.

        This method assumes there is a method to retrieve city instances by state ID.
        """
        from models import storage
        return [city for city in storage.all("City").values() if city.state_id == self.id]
