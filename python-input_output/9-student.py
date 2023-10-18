#!/usr/bin/python3
"""Class Student definition"""


class Student:
    """Create a student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(obj):
        """ function that returns the dictionary description"""
        dictionary = {}
        if hasattr(obj, "__dict__"):
            dictionary = obj.__dict__.copy()

        return dictionary
