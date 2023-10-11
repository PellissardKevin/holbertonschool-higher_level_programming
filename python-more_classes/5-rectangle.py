#!/usr/bin/python3
"""Contains an empty class definition of 'Rectangle'"""


class Rectangle:
    """definition of 'Rectangle'"""

    def __init__(self, width=0, height=0):
        if not type(width) is int:
            raise TypeError("width must be an integer")
        elif not type(height) is int:
            raise TypeError("height must be an integer")
        if int(width) < 0:
            raise ValueError("width must be >= 0")
        if int(height) < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        self.__width = width

    @property
    def height(self):
        return self.__height

    @property
    def width(self):
        return self.__width

    @height.setter
    def height(self, value):
        if not type(value) is int:
            raise TypeError("height must be an integer")
        elif int(value) < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @width.setter
    def width(self, value):
        if not type(value) is int:
            raise TypeError("width must be an integer")
        elif int(value) < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        return self.__height * 2 + self.__width * 2

    def my_print(self):
        """Prints a square with '#'"""
        if self.__width == 0 or self.__height == 0:
            print()
            return
        print("{}".format("\n".join(["#" * self.__width] * self.__height)))

    def __str__(self):
        string = ""
        if self.__width == 0 or self.__height == 0:
            return string
        string += "{}".format("\n".join(["#" * self.__width] * self.__height))
        return string

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        print("Bye rectangle...")
