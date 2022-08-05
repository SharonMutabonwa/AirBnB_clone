#!/usr/bin/python3
"""A module that represents a class BaseModel"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    '''Defines all common attributes/methods for other classes'''

    def __init__(self, *args, **kwargs):
        '''Contructor method'''

        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())  # instance attribute
        self.created_at = datetime.now()  # instance attribute
        self.updated_at = datetime.now()  # instance attribute

        if kwargs:
            for key, value in kwargs.item():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, tform)
        else:
            storage.new(self)

    def __str__(self):
        '''Prints in a string format'''

        print("[{}] ({}) {}".format(self.__class__.name,
              self.id, self.__dict__))

    def save(self):
        '''updates the public instance attribute updated_at
        with the current datetime'''

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        '''returns a dictionary containing all keys/values
        of __dict__ of the instance'''

        new_dict = self.__dict__.copy()
        new_dict["__class__"] = type(self).__name__
        new_dict["created_at"] = new_dict["created_at"].isoformat()
        new_dict["updated_at"] = new_dict["updated_at"].isoformat()
        return new_dict
