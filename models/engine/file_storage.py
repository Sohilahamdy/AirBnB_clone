#!/usr/bin/python3
# models/engine/file_storage.py

from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class FileStorage:
    """Handles in-memory storage of BaseModel objects."""

    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of all objects or objects of a specific class."""
        if cls is None:
            return FileStorage.__objects
        result = {}
        for key, obj in FileStorage.__objects.items():
            if isinstance(obj, cls):
                result[key] = obj
        return result

    def new(self, obj):
        """Adds a new object to storage."""
        if obj:
            key = f"{obj.__class__.__name__}.{obj.id}"
            FileStorage.__objects[key] = obj

    def save(self):
        """Save all objects to file (for this example, we'll just pass)."""
        pass

    def reload(self):
        """Reload objects from file (for this example, we'll just pass)."""
        pass

    def get(self, cls, id):
        """Retrieve one object by class and ID."""
        key = f"{cls.__name__}.{id}"
        return FileStorage.__objects.get(key)

    def count(self, cls=None):
        """Count the number of objects in storage."""
        if cls is None:
            return len(FileStorage.__objects)
        return len(self.all(cls))
        
    def delete(self, obj=None):
        """Delete an object from storage."""
        if obj:
            key = f"{obj.__class__.__name__}.{obj.id}"
            if key in FileStorage.__objects:
                del FileStorage.__objects[key]

    def update(self, obj):
        """Update an object in storage."""
        if obj:
            key = f"{obj.__class__.__name__}.{obj.id}"
            FileStorage.__objects[key] = obj
