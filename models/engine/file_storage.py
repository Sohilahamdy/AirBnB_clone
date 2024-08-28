#!/usr/bin/python3

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from json.decoder import JSONDecodeError


class FileStorage():
    """Reloads the stored objects from the file"""

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns a dictionary of all objects in storage."""
        return FileStorage.__objects

    def new(self, obj):
        """Adds a new object to storage."""
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            FileStorage.__objects[key] = obj

    def save(self):
        """Save method documentation"""
        with open(FileStorage.__file_path, 'w') as file:
            json.dump({key: obj.to_dict() for key, obj in FileStorage.__objects.items()}, file)

    def reload(self):
        """Reloads the stored objects from the file"""
        try:
            with open(FileStorage.__file_path, 'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name = value['__class__']
                    cls = globals()[class_name]
                    FileStorage.__objects[key] = cls(**value)

        except FileNotFoundError:
            pass
