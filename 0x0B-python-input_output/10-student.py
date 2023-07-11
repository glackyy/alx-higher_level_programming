#!/usr/bin/python3
"""Defining Student class"""


class Student:
    """This class defines a student

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns the dict representation of the student instance"""
        if attrs is None:
            attrs = self.__dict__.keys()
        else:
            attrs = set(attrs)

        json_dic = {}
        for attrib in attrs:
            if attrib in self.__dict__:
                json_dic[attrib] = self.__dict__[attrib]
        return json_dic
