#!/usr/bin/python3
# models/engine/file_storage.py

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class FileStorage:
    """This class manages storage of hbnb models in JSON format"""

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns a dictionary of all objects"""
        return self.__objects

    def new(self, obj):
        """Adds a new object to the storage"""
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """Saves the objects to a JSON file"""
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects (if it exists)"""
        try:
            with open(self.__file_path, 'r') as f:
                obj_dict = json.load(f)
                print("Contents loaded from file:")
                print(obj_dict)  # Add this line to print contents
                for key, value in obj_dict.items():
                    class_name = value['__class__']
                    cls = globals().get(class_name)
                    if cls:
                        self.__objects[key] = cls(**value)
                    else:
                        print(f"Class {class_name} not found.")
        except FileNotFoundError:
            pass
