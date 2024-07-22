#!/usr/bin/python3
# models/amenity.py

from models.base_model import BaseModel

class Amenity(BaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = ""

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {{'id': '{self.id}', 'created_at': {self.created_at}, 'updated_at': {self.updated_at}, 'name': '{self.name}'}}"
