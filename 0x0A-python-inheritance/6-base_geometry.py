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
