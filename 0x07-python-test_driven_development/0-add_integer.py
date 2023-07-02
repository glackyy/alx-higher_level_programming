#!/usr/bin/python3

"""Defining an integer addition func."""


def add_integer(a, b=98):
    """Adds two integers.
    
    Args:
        a: (int)
        b: (int)

    Returns: int
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")
    return int(a) + int(b)
