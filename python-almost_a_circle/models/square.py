#!/usr/bin/python3
"""Class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square inherit of Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.__size = size
        self.__x = x
        self.__y = y

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not type(value) is int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value

    def __str__(self):
        """return a strings for print"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
            self.id, self.__x, self.__y, self.__size)

    def update(self, *args, **kwargs):
        """Definition update with variadic function"""
        for key, value in kwargs.items():
            setattr(self, key, value)

