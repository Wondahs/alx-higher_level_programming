#!/usr/bin/python
"""Defines a square"""


class Square:
    """ An empty class that defines a Square

    Attributes:
    __size (int): Size of square. Size must be at least 0
    """
    def __init__(self, size=0):
        """init module.

        Args:
            size (int): Size of square.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """ Returns the size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ Sets new value to size

        Args:
            value: New value
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ Calculates the area of square

        Args:
            self: Instance of square

        Return:
            Area of square size
        """
        return (self.__size * self.__size)

    def my_print(self):
        """ Prints square
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end='')
                print()
