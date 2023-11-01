#!/usr/bin/python3
"""Module that handles multiplication of matrices using numpy"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Function that performs matrix multiplication of m_a and m_b"""

    result = np.matmul(m_a, m_b)

    return result
