#!/usr/bin/python3
"""Defining a Rectangle subclass Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class representing a Square.Inherits from Rectangle"""

    def __init__(self, size):
        """Initialize a Square

        Args:
            size (int): The size of the square
        Raises:
            TypeError: If size is not an integer
            ValueError: If size is not a positive integer
        """
        self.__size = size
        self.integer_validator("size", self.__size)
        super().__init__(self.__size, self.__size)

    def __str__(self):
        """Return a string representation of the Square"""
        return "[Square] {}/{}".format(self.__size, self.__size)

