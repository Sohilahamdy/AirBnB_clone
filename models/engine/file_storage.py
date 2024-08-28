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
        if cls is None:
            return self.__objects
        class_name = cls.__name__
        return {k: v for k, v in self.__objects.items() if k.startswith(class_name)}

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
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key, obj_dict in data.items():
                    cls_name = obj_dict.get('__class__')
                    if cls_name:
                        cls = globals().get(cls_name)
                        if cls:
                            obj = cls(**obj_dict)
                            self.__objects[key] = obj
                        else:
                            print(f"** class '{cls_name}' not found **")
                    else:
                        print("** no '__class__' key found **")
        except FileNotFoundError:
            print("** file not found **")
        except JSONDecodeError:
            print("** error decoding JSON **")
        except Exception as e:
            print(f"** unexpected error: {e} **")
