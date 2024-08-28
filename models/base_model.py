#!/usr/bin/python3

import uuid
from datetime import datetime
import models


class BaseModel:
    """A base class for all models"""

    def __init__(self, *args, **kwargs):
        """Description of the OtherModel class."""
        if kwargs:
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Return a string representation of the instance."""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """Update the 'updated_at' attribute with the current time and save
        the instance to storage."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Convert the instance to a dictionary representation."""
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.__dict__['created_at'].isoformat()
        new_dict['updated_at'] = self.__dict__['updated_at'].isoformat()
        return (new_dict)
