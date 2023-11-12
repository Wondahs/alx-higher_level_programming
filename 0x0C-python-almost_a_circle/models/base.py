#!/usr/bin/python3
"""Module containing base class"""
import json
import csv


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
            new_list = [obj.to_dictionary() for obj in list_objs]
            file.write(Base.to_json_string(new_list))

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation json_string.
        """
        if json_string in ["", None]:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set.
        """
        if not dictionary or dictionary == {}:
            return
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def create_from_list(cls, cls_as_list):
        """
        Returns an instance from list.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        c_as_l = tuple(cls_as_list)
        dummy.update(*c_as_l)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances.
        """
        result = []
        filename = f"{cls.__name__}.json"

        try:
            with open(filename, 'r', encoding='utf-8') as file:
                j_str = file.read()
                dict_list = cls.from_json_string(j_str)
                for item in dict_list:
                    result.append(cls.create(**item))
                return result
        except FileNotFoundError:
            return result

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes in CSV and writes to csv file"""
        result = []
        if list_objs in [[], None]:
            return result
        if cls.__name__ == "Rectangle":
            header = ["id", "width", "height", "x", "y"]
        elif cls.__name__ == "Square":
            header = ["id", "size", "x", "y"]
        result.append(header)
        for obj in list_objs:
            result.append(obj.to_list())
        filename = f"{cls.__name__}.csv"
        with open(filename, 'w', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(result[0])
            writer.writerows(result[1:])

    @classmethod
    def load_from_file_csv(cls):
        """Reads CSV and deserializes"""
        filename = f"{cls.__name__}.csv"
        result = []
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    int_row = [int(element) for element in row]
                    result.append(cls.create_from_list(int_row))
                return result
        except IOError:
            return result
