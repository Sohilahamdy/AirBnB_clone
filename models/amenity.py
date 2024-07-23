#!/usr/bin/python3
# models/amenity.py

from models.base_model import BaseModel

class Amenity(BaseModel):
    """Amenity class that inherits from BaseModel"""

    name = ""

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) name: {self.name}"
