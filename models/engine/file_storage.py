#!/usr/bin/python3
"""Defines a FileStorage class"""
import json


class FileStorage:
    '''serializes instances to a JSON file
    and deserializes JSON file to instances'''

    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''returns the dictionary __objects'''
        return self.__object

    def new(self, obj):
        '''sets in __objects the obj with key <obj class name>.id'''
        self.__object["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        '''serializes __objects to the JSON file (path: __file_path)'''
        object_dict = {}
        for key in self.__object:
            object_dict = self.__object[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(object_dict, f)

    def reload(self):
        '''deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists'''
        if self.__file_path:
            with open(self.__file_path, 'r') as f:
                object_dict = json.load(f)
