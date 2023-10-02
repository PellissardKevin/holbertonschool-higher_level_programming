#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        x = '\n'.join([' '.join(['{}'.format(item) for item in row])])
        print(x)
