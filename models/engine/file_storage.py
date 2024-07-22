##!/usr/bin/python3
# models/engine/file_storage.py

import json
from models.base_model import BaseModel

class FileStorage:
    __objects = {}
    __file_path = "file.json"

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        with open(FileStorage.__file_path, "w") as f:
            json.dump({key: obj.to_dict() for key, obj in FileStorage.__objects.items()}, f)

    def reload(self):
        try:
            with open(FileStorage.__file_path, "r") as f:
                objs = json.load(f)
                for key, value in objs.items():
                    cls = globals()[value["__class__"]]
                    FileStorage.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass
