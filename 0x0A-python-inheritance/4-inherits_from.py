#!/usr/bin/python3
"""Defining a function inherits_from"""


def inherits_from(obj, a_class):
    """Checks if the object is inheritated instance of the class

    Args:
        obj: the object to check
        a_class: the class to compare against
    Returns:
        True if the object is inheritaded instance of the class
        False otherwise
    """
    return (
        issubclass(type(obj), a_class) and
        type(obj) is not a_class)
