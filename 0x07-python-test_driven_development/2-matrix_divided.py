#!/usr/bin/python3
"""A module that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """
    Function that divides numbers in matrix
    """

    if (not isinstance(matrix, list) or
        not (all(isinstance(row, list) for row in matrix)) or
        not (all(isinstance(element, (int, float))
             for row in matrix for element in row))):
        raise TypeError("matrix must be a matrix (list "
                        "of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    result = [row[:] for row in matrix]

    for row in result:
        for i in range(len(row)):
            row[i] = float("{:.2f}".format(row[i] / div))
    return result
