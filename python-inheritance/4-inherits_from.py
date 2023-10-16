#!/usr/bin/python3
""" Definition of inherits_from function"""


def inherits_from(obj, a_class):
    """  function that returns True if the object is an
    instance of a class that inherited """
    if type(obj) == a_class:
        return False
    else:
        return isinstance(obj, a_class)
