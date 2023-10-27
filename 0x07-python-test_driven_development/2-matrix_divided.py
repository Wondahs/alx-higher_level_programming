#!/usr/bin/python3
"""A module that divides all elements of a matrix"""


def matrix_divided(matrix, div):
	if (not isinstance(matrix, list)
		or not (all(isinstance(row, list) for row in matrix))
		or not (all(isinstance(element, (int, float)) for row in matrix for element in row))
		):
		raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
	if not all(len(row) == len(matrix[0]) for row in matrix):
		raise TypeError("Each row of the matrix must have the same size")
	if not isinstance(div, (int, float)):
		raise TypeError("div must be a number")
	if div == 0:
		raise ZeroDivisionError("division by zero")

	result = matrix.deepcopy(matrix)

	for row in result:
		for element in row:
			element = {:.2f}.format(element / div)
	return result