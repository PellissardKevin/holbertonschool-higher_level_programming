#!/usr/bin/python3
"""Definition of class to json funtion"""


def class_to_json(obj):
    """function that returns the dictionary
    description"""
    dictionary = {}
    if hasattr(obj, "__dict__"):
        dictionary = obj.__dict__.copy()

    return dictionary
