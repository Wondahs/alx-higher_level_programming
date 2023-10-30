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
        """Sets and gets width"""
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
        """Sets and gets height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value

    def area(self):
        """Calculates and returns area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates and returns area of rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        perimeter = 2 * (self.__width + self.__height)
        return perimeter
