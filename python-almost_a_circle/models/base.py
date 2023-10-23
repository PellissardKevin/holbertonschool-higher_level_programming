#!/usr/bin/python3
"""Create class Base"""
import json


class Base:
    """Class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns JSON string"""
        if list_dictionaries is None:
            return '[]'
        return json.dumps(list_dictionaries)
