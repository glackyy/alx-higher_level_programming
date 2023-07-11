#!/usr/bin/python3
"""Defining Student class"""


class Student:
    """This class defines a student

    Attributes:
        first_name (str): first name of the student
        last_name (str): last name of the student
        age (int): the age of the student
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns te dict representation of the student instance"""
        json_dic = {
             'first_name': self.first_name,
             'last_name': self.last_name,
             'age': self.age
          }
        return json_dic
