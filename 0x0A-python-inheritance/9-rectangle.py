#!/usr/bin/python3
"""Defining a class Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class representing a Rectangle.Inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Initialize a Rectangle

        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
        Raises:
            TypeError: If width or height is not an integer
            ValueError: If width or height is not a positive integer
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)

    def area(self):
        """Compute the area of the rectangle

        Returns:
            int: The area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Return a string representation of the Rectangle

        Returns:
            str: The string representation of the Rectangle
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
