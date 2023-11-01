#!/usr/bin/python3
"""Module that handles multiplication of matrices using numpy"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Function that performs matrix multiplication of m_a and m_b"""

    mat1 = np.array(m_a)
    mat2 = np.array(m_b)

    result = np.dot(mat1, mat2)

    return result
