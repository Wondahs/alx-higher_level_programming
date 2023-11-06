#!/usr/bin/python3
"""Module that defines a Rectangle class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defines Rectangle based on BaseGeometry"""

    def __init__(self, width, height):
        """Instantiates BaseGeometry object"""

        self.integer_validator("height", height)
        self.__height = height
        self.integer_validator("width", width)
        self.__width = width

    def area(self):
        """Returns area of Rectangle"""

        return self.__height * self.__width

    def __str__(self):
        """Returns printable representation of Rectangle"""

        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
