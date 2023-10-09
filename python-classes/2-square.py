#!/usr/bin/python3
"""Contains a class definition of 'Square'"""


class Square:
    """Definition of size in square"""
    def __init__(self, size=0):
        if not type(size) is int:
            raise TypeError("size must be an integer")
        if int(size) < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
