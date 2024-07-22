#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class FileStorage:
    """Handles storage of objects using JSON format."""
    
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns a dictionary of all stored objects.
        Each key is formatted as '<class_name>.<object_id>'.
        """
        return self.__objects

    def new(self, obj):
        """
        Adds a new object to storage.
        Args:
            obj (BaseModel): The object to add.
        """
        if not isinstance(obj, BaseModel):
            raise TypeError("obj must be an instance of BaseModel")
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        Saves all objects to the JSON file.
        """
        with open(self.__file_path, 'w') as file:
            json.dump(
                {key: obj.to_dict() for key, obj in self.__objects.items()},
                file
            )

    def reload(self):
        """
        Loads objects from the JSON file into memory.
        """
        try:
            with open(self.__file_path, 'r') as file:
                objects = json.load(file)
                for key, obj_data in objects.items():
                    class_name = key.split('.')[0]
                    cls = self.__get_class(class_name)
                    if cls:
                        self.__objects[key] = cls(**obj_data)
        except FileNotFoundError:
            pass
        except json.JSONDecodeError:
            print(f"Warning: {self.__file_path} is empty or corrupt.")

    def get(self, cls, id):
        """
        Retrieves an object by class and ID.
        Args:
            cls (type): The class type of the object to retrieve.
            id (str): The ID of the object to retrieve.
        Returns:
            BaseModel: The object with the specified class and ID, or None if not found.
        """
        if not issubclass(cls, BaseModel):
            raise TypeError("cls must be a subclass of BaseModel")
        key = f"{cls.__name__}.{id}"
        return self.__objects.get(key)

    def __get_class(self, class_name):
        """
        Retrieves the class based on the class name.
        Args:
            class_name (str): The name of the class.
        Returns:
            class: The class associated with the class_name.
        """
        class_map = {
            'BaseModel': BaseModel,
            'User': User,
            'Place': Place,
            'State': State,
            'City': City,
            'Amenity': Amenity,
            'Review': Review
        }
        return class_map.get(class_name)

    def delete(self, obj=None):
        """
        Deletes an object from storage.
        Args:
            obj (BaseModel, optional): The object to delete. If None, do nothing.
        """
        if obj is None:
            return
        key = f"{obj.__class__.__name__}.{obj.id}"
        if key in self.__objects:
            del self.__objects[key]

    def update(self, obj):
        """
        Updates an existing object in storage.
        Args:
            obj (BaseModel): The object to update.
        """
        if not isinstance(obj, BaseModel):
            raise TypeError("obj must be an instance of BaseModel")
        key = f"{obj.__class__.__name__}.{obj.id}"
        if key in self.__objects:
            self.__objects[key] = obj
        else:
            raise KeyError(f"No such object: {key}"

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
