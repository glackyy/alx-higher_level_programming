#!/usr/bin/python3
"""Defining a function is kind of class."""


def is_kind_of_class(obj, a_class):
    """Check if the object is an instance or inherited instance of a class.

    Args:
        obj (any): The object to check
        a_class (type): The class to match the type of obj
    Returns:
           if obj is instance or inheritd True
           Otherwise False
    """
    return isinstance(obj, a_class)
