#!/usr/bin/python3
"""Class Student definition"""


class Student:
    """Create a student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """function that returns the dictionary description"""
        if ((type(attrs) is list) and all((type(x) is str) for x in attrs)):
            return {x: getattr(self, x) for x in attrs if hasattr(self, x)}
        return self.__dict__

    def reload_from_json(self, json):
        """ replaces attributes of the Student instance """
        for i in json:
            self.__dict__[i] = json[i]
