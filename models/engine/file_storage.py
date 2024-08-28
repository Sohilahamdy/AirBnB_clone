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
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, mode='w') as my_file:
            json.dump(new_dict, my_file)

    def reload(self):
        """Reloads the stored objects from the file"""
        if not os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'w') as file:
                file.write('{}')  # Create an empty JSON file

        try:
            with open(FileStorage.__file_path, mode='r') as my_file:
                new_dict = json.load(my_file)

            for key, value in new_dict.items():
                class_name = value.get('__class__')
                obj = eval(class_name + '(**value)')
                FileStorage.__objects[key] = obj

        except FileNotFoundError:
            pass
        except JSONDecodeError:
            pass
