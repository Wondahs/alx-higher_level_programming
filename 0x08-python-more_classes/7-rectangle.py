#!/usr/bin/python3
""" Module that defines a rectangle."""


class Rectangle:
    """Class defining rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialises rectangle"""

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
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

    def __str__(self):
        """Returns a printable rectangle"""
        if self.__height == 0 or self.__width == 0:
            return ""
        result = ""
        for _ in range(self.__height):
            result += str(self.print_symbol) * self.__width + "\n"

        return result.rstrip("\n")

    def __repr__(self):
        """Returns a representation of the rectangle
        to be able to recreate a new instance by using eval()
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Prints message when an instance of Rectangle is deleted,
        and decrements number_of_instances.
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
