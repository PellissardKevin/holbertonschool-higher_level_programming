#!/usr/bin/python3
"""divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix."""
    invalid_mat = "matrix must be a matrix (list of lists) of integers/floats"
    if not type(matrix) is list or len(matrix) == 0:
        raise TypeError(invalid_mat)
    if not type(div) is int and not type(div) is float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    row_length = None
    for row in matrix:
        if not type(row) is list or len(row) == 0:
            raise TypeError(invalid_mat)
        if row_length is not None and row_length != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        row_length = len(row)
        for col in row:
            if not type(col) is int and not type(col) is float:
                raise TypeError(invalid_mat)

    return [[round(col / div, 2) for col in row] for row in matrix]
