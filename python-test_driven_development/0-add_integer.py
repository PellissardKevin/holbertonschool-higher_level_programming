#!/usr/bin/python3
""" Return the addition of two integer
>>> add_integer(5, 10)
15
>>> add_integer(2)
100"""


def add_integer(a, b=98):
    """Computes the sum of two integers
        return error if a or b is not interger
    """
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    elif not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
