#!/usr/bin/python3
def add_integer(a, b=98):
    """Computes the sum of two integers"""
    if not (type(a) is int) or (type(a) is float):
        raise TypeError("a must be an integer")
    elif not (type(b) is int) or (type(b) is float):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
