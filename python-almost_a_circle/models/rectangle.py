#!/usr/bin/python3
"""Class Rectangle inherit from Base"""


from models.base import Base


class Rectangle(Base):
    """ Class Rectangle inherit Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, value):
        if not type(value) is int:
            raise TypeError("width must be an integer")
        elif int(value) < 0:
            raise ValueError("width must be >= 0")
        self.width = value

    @height.setter
    def height(self, value):
        if not type(value) is int:
            raise TypeError("height must be an integer")
        elif int(value) < 0:
            raise ValueError("height must be >= 0")
        self.height = value

    @x.setter
    def x(self, value):
        if not type(value) is int:
            raise TypeError("x must be an integer")
        elif int(value) < 0:
            raise ValueError("x must be >= 0")
        self.x = value

    @y.setter
    def y(self, value):
        if not type(value) is int:
            raise TypeError("y must be an integer")
        elif int(value) < 0:
            raise ValueError("y must be >= 0")
        self.y = value
