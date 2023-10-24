#!/usr/bin/python
"""Defines a square"""


class Square:
    """An empty class that defines a Square.

    Attributes:
        __size (int): Size of square
    """

    def __init__(self, size=0):
        """init module.
        Args:
            size (int): Size of square.
        """
        self.__size = size

    @property
    def size(self):
        """Returns the size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculates the area of square."""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints square with "#" character"""
        if self.__size == 0:
            print()
            return
        else:
            for i in range(self.__size):
                [print("#", end="") for j in range(self.__size)]
                print()
