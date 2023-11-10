#!/usr/bin/python3
"""Module containing base class"""


class Base:
    """Base class"""
    __nb_objects = 0
    def __init__(self, id=None):
        """Instantiates Base object"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries.
        list_dictionaries is a list of dictionaries.
        """
        import json


        if list_dictionaries in "[], None":
            return "[]"
        return json.dumps(list_dictionaries)
