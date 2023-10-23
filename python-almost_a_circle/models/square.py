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
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not type(value) is int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not type(value) is int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not type(value) is int:
            raise TypeError("x must be an integer")
        if value < 0:
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

    def __str__(self):
        """return a strings for print"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
            self.id, self.__x, self.__y, self.__size)
