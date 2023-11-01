#!/usr/bin/python3
"""Module that handles multiplication of matrices using numpy"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Function that performs matrix multiplication of m_a and m_b"""

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if m_a in [[], [[]]]:
        raise ValueError("m_a can't be empty")
    if m_b in [[], [[]]]:
        raise ValueError("m_b can't be empty")
    if not all(isinstance(element, (int, float))
               for row in m_a for element in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(element, (int, float))
               for row in m_b for element in row):
        raise TypeError("m_b should contain only integers or floats")
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    mat1 = np.array(m_a)
    mat2 = np.array(m_b)

    result = np.dot(mat1, mat2)

    return result
