#!/usr/bin/python3
"""A module for addition"""


def add_integer(a, b=98):
    """
    Function that adds a and b

    >>> add_integer(1, 3)
    4
    >>> add_integer(2)
    100

    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)

    return a + b
