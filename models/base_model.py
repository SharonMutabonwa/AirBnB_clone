#!/usr/bin/python3
<<<<<<< HEAD
"""Module for Base class
Contains the Base class for the AirBnB clone console.
"""

=======
"""A module that represents a class BaseModel"""
>>>>>>> 73a8d997822c80c5e1e76d5e5c115f236047c773
import uuid
from datetime import datetime
from models import storage


class BaseModel:
<<<<<<< HEAD

    """Class for base model of object hierarchy."""

    def __init__(self, *args, **kwargs):
        """Initialization of a Base instance.

        Args:
            - *args: list of arguments
            - **kwargs: dict of key-values arguments
        """

        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Returns a human-readable string representation
        of an instance."""

        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Updates the updated_at attribute
        with the current datetime."""
=======
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
>>>>>>> 73a8d997822c80c5e1e76d5e5c115f236047c773

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
<<<<<<< HEAD
        """Returns a dictionary representation of an instance."""

        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
=======
        '''returns a dictionary containing all keys/values
        of __dict__ of the instance'''

        new_dict = self.__dict__.copy()
        new_dict["__class__"] = type(self).__name__
        new_dict["created_at"] = new_dict["created_at"].isoformat()
        new_dict["updated_at"] = new_dict["updated_at"].isoformat()
        return new_dict
>>>>>>> 73a8d997822c80c5e1e76d5e5c115f236047c773
