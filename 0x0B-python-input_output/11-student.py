#!/usr/bin/python3
"""Defining Student class"""


class Student:
    """represents a student"""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the Student.

        Args:
            attrs (list): (Optional) The attributes to represent.
        """
        if attrs is None:
            attrs = self.__dict__.keys()
        else:
            attrs = set(attrs)

        json_dic = {}
        for attrib in attrs:
            if attrib in self.__dict__:
                json_dic[attrib] = self.__dict__[attrib]

        return json_dic

    def reload_from_json(self, json):
        """Replaces all attributes of the student based on a dict

        Args:
            json (dict): The dict containing attr names and values
        """
        for k, v in json.items():
            setattr(self, k, v) 
