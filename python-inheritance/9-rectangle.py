#!/usr/bin/python3
""" Class BaseGemotry"""


class BaseGeometry:
    """Class BaseGeometry"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))

    class Rectangle(BaseGeometry):
        """class Rectangle, inherit of BaseGeometry"""
        def __init__(self, width, height):
            self.__width = width
            self.__height = height
            self.integer_validator("width", width)
            self.integer_validator("height", height)

        def area(self):
            return self.__height * self.__width

        def __str__(self):
            return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
