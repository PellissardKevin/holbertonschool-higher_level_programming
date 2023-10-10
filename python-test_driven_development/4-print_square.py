#!/usr/bin/python3
""" prints a square with the character '#'"""


def print_square(size):
    """print a square with a size
    return an error if size it's not an integer
    or if size less than 0"""
    if not type(size) is int:
        raise TypeError("size must be an integer")
    if int(size) < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")

    print("{}".format(("#" * size + "\n") * size), end="")
