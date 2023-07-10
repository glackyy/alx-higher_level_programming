#!/usr/bin/python3
"""Defining a class BaseGeometry"""


class BaseGeometry:
    """A class representing Base Geometry"""

    def area(self):
        """Compute the area of the geometry

        Raises:
              Exception: Indicates that the area is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate the value as an integer

        Args:
            name: The name of the value
            value: The value to be validated

        Raises:
              TypeError: if value is not integer
              ValueError: if value is <= 0
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
