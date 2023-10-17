#!/usr/bin/python3
""" Class that inherits from BaseGeometry """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ class Square that inherits from Rectangle """

    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        return super().area()

    def __str__(self):
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
