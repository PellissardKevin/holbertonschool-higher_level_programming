#!/usr/bin/python3
"""Contains a class definition of 'Square'"""


class Square:
    """Definition of size in square"""

    def __init__(self, size=0, position=(0, 0)):
        if not type(size) is int:
            raise TypeError("size must be an integer")
        if int(size) < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        if not type(value) is int:
            raise TypeError("size must be an integer")
        if int(value) < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        if not type(value) is int:
            raise TypeError("size must be an integer")
        if not type(value) is tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size <= 0 or self.__position[1] > 0:
            print("")

        for i in range(self.__size):
            for k in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print("")
