#!/usr/bin/python3
"""Define a class Square."""

class Square:
    """represents a Square."""

    def __init__(self, size=0):
        """Initialize an instance of the class.

        Args:
            size (int): The size of the new square."""

        self.size = size
        
    @property
    def size(self):
        """Getter retrieving the size of the square."""

        return self.__size

    @size.setter
    def size(self,value):
        """Setter for setting The size of the square."""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current area of the square."""
        return self.__size ** 2
