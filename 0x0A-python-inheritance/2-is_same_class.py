#!/usr/bin/python3

"""Defining a function is_name_class"""


def is_name_class(obj, a_class):
    """Checks if the object is exactly an instance of the class

    Args:
        obj: The object to check
        a_class: the class to compare
    Returns:
           True
    """
    return type(obj) is a_class
