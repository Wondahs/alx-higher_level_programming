#!/usr/bin/python3
""" Module that defines a rectangle."""


class Rectangle:
    """Class defining rectangle"""

    def __init__(self, width=0, height=0):
        """Initialises rectangle"""

        self.width = width
        self.height = height

    @property
    def width(self):
        """Sets and retrives width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Sets and retrives height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
