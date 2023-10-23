#!/usr/bin/python3
"""Class Rectangle inherit from Base"""


from models.base import Base


class Rectangle(Base):
    """ Class Rectangle inherit Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        if not type(width) is int:
            raise TypeError("width must be an integer")
        if int(width) < 0:
            raise ValueError("width must be >= 0")
        if not type(height) is int:
            raise TypeError("height must be an integer")
        if int(height) < 0:
            raise ValueError("height must be >= 0")
        if not type(x) is int:
            raise TypeError("x must be an integer")
        if int(x) < 0:
            raise ValueError("x must be >= 0")
        if not type(y) is int:
            raise TypeError("y must be an integer")
        if int(y) < 0:
            raise ValueError("y must be >= 0")
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not type(value) is int:
            raise TypeError("width must be an integer")
        if int(value) < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not type(value) is int:
            raise TypeError("height must be an integer")
        if int(value) < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not type(value) is int:
            raise TypeError("x must be an integer")
        if int(value) < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not type(value) is int:
            raise TypeError("y must be an integer")
        if int(value) < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
