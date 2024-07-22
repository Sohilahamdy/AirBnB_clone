#!/usr/bin/python3
# models/engine/file_storage.py

import json
from models.base_model import BaseModel

class FileStorage:
    """This class manages storage of hbnb models in JSON format"""

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns a dictionary of all objects"""
        return self.__objects

    def new(self, obj):
        """Adds a new object to the storage"""
        if obj:
            key = f"{obj.__class__.__name__}.{obj.id}"
            self.__objects[key] = obj

    def save(self):
        """Saves the objects to a JSON file"""
        with open(self.__file_path, 'w') as f:
            obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
            json.dump(obj_dict, f)

    def reload(self):
        """Loads objects from a JSON file"""
        try:
            with open(self.__file_path, 'r') as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    cls_name = value['__class__']
                    cls = BaseModel.__subclasses__()[0]  # Adjust based on your class hierarchy
                    self.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass
