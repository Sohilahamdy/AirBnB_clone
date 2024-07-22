#!/usr/bin/python3
# models/base_model.py

import uuid
from datetime import datetime
from models.engine.file_storage import FileStorage

class BaseModel:
    """Base class for all models in the AirBnB clone."""

    storage = FileStorage()  # Initialize storage

    def __init__(self, *args, **kwargs):
        """Initializes a new BaseModel."""
        if kwargs:
            for key, value in kwargs.items():
                if key in ['created_at', 'updated_at']:
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            self.save()

    def __str__(self):
        """Returns a string representation of the instance."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the 'updated_at' attribute and saves to storage."""
        self.updated_at = datetime.utcnow()
        self.__class__.storage.new(self)
        self.__class__.storage.save()

    def to_dict(self):
        """Returns a dictionary representation of the instance."""
        dict_representation = self.__dict__.copy()
        dict_representation["__class__"] = self.__class__.__name__
        dict_representation["created_at"] = self.created_at.isoformat()
        dict_representation["updated_at"] = self.updated_at.isoformat()
        return dict_representation
