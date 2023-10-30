#!/usr/bin/python3
"""A module that prints squares"""


def print_square(size):
    """A function that prints squares.

    Args:
        size (int): Size of square.

    Raises:
        TypeError: if size is not an integer,
                   or if size is a float and int(size) is less than 0.
        ValueError: if size is less than 0
    """
    if isinstance(size, float):
        if int(size) < 0:
            raise TypeError("size must be an integer")
    elif not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    size = int(size)
    for _ in range(1, size + 1):
        print("#" * size)
