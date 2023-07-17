#!/usr/bin/python3

"""Defining Base class"""
import json
import csv


class Base:
    """managing id attribute in future classes

    Attributes:
        __nb_objects (int): Private class attrib
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the Base object

        Args:
            id (int, optional): Unique id for the object
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of a list dict"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file

        Args:
            list_objs (list): a list of instances
        """
        f_name = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []
        l_dicts = [obj.to_dictionary() for obj in list_objs]
        js_str = cls.to_json_string(l_dicts)
        with open(f_name, 'w') as file:
            file.write(js_str)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list represented by the JSON string"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances created from a JSON file"""
        f_name = cls.__name__ + ".json"
        try:
            with open(f_name, 'r') as file:
                js_str = file.read()
                l_dict = cls.from_json_string(js_str)
                return [cls.create(**d) for d in l_dict]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV serialization of a list of objects to a file.

        Args:
            list_objs (list): A list of inherited Base instances.
        """
        f_name = cls.__name__ + ".csv"
        with open(f_name, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file.

        Reads from `<cls.__name__>.csv
        """
        f_name = cls.__name__ + ".csv"
        try:
            with open(f_name, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                l_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                l_dicts = [dict([k, int(v)] for k, v in d.items())
                           for d in list_dicts]
                return [cls.create(**d) for d in l_dicts]
        except IOError:
            return []
