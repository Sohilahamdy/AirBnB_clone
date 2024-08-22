#!/usr/bin/python3

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class that inherits from BaseModel"""

    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize a Amenity instance."""
        super().__init__(*args, **kwargs)
