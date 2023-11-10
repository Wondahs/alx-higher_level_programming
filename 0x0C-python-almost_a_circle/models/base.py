#!/usr/bin/python3
"""Module containing base class"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries.
        list_dictionaries is a list of dictionaries.
        """
        if list_dictionaries in [[], None]:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file.
        """
        filename = f"{cls.__name__}.json"

        with open(filename, 'w', encoding='utf-8') as file:
            if list_objs is None:
                file.write("[]")
            new_list = [obj.to_dictionary() for obj in list_objs ]
            file.write(Base.to_json_string(new_list))
