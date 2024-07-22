#!/usr/bin/python3
# models/amenity.py
from models.base_model import BaseModel

class Amenity(BaseModel):
    """Represent an Amenity in the AirBnB system."""

    def __init__(self, name="", *args, **kwargs):
        """Initialize an Amenity instance."""
        super().__init__(*args, **kwargs)
        self.name = name

    def __str__(self):
        """Return a string representation of the Amenity instance."""
        return f"[Amenity] ({self.id}) {self.__dict__}"
