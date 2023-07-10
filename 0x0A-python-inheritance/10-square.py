#!/usr/bin/python3
"""Defining a class Square"""


class Square(Rectangle):
    """A class representing a Square.Inherits from Rectangle"""

    def __init__(self, size):
        """Initialize a Square

        Args:
            size (int): The size of the square
        Raises:
            TypeError: if size is not an integer
            ValueError: if size in not a positive integer
        """
        self.__size = size
        self.integer_validator("size", self.__size)
        super().__init__(self.__size, self.__size)

    def __str__(self):
        """Return a string representation of the Square"""
        return "[Square] {}/{}".format(self.__size, self.__size)
