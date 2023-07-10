#!/usr/bin/python3
"""Defining a class Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class representing a Rectangle.Inherited from BaseGeometry"""

    def __init__(self, width, height):
        """Initialize a Rectangle

        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
        Raises:
              TypeError: if width or height is not an integer
              ValueError: if width or height in not a positive integer
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)

    def __str__(self):
        """Returns a string representation of the Rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
