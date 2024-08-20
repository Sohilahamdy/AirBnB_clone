#!/usr/bin/python3

import uuid
from datetime import datetime

try:
    from dateutil.parser import parse as parse_date
except ImportError:
    parse_date = None

class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    if parse_date:
                        value = parse_date(value)
                    else:
                        value = datetime.fromisoformat(value)
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            

    def __str__(self):
        """Returns a string representation of the instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()
        from models import storage
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Return a dictionary representation of the instance."""
        dict_representation = {
                '__class__': self.__class__.__name__,
                'id': self.id,
                'created_at': self.created_at.isoformat(),
                'updated_at': self.updated_at.isoformat(),
        }
        for key, value in self.__dict__.items():
            if key not in ['_sa_instance_state', 'created_at', 'updated_at']:
                dict_representation[key] = value
        return dict_representation
