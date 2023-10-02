#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in range(len(matrix)):
        for val in range(len(matrix[row])):
            print("{}".format(matrix[row][val]), end="")
            if val != len(matrix[0]) - 1:
                print(" ", end="")
        print()
