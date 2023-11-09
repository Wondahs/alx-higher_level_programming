#!/usr/bin/python3
"""Module containing Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class that defines Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Instantiates Square object"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """
        Return the print() and str() representation of a Square.
        """
        string = ""
        string += f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
        return string
