#!/usr/bin/python3
"""class square """

BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class of a square"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area():
        return self.__size ** 2

    def __str__(self):
        return "[square] {:d}/{:d}".format(self.__width, self.__height)
