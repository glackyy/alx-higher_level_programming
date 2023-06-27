#!/usr/bin/python3

"""Define class Square."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initialize a Square instance.

        Args:
            size (float or int): The size of the square.
        """
        self.size = size

    @property
    def size(self):
        """Returns the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (float or int): The size of the square.
        """
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of the square."""
        return self.size ** 2

    def __equals__(self, other):
        """Check if two squares have equal areas.

        Args:
            other (Square): The other square to compare.
        """
        return self.area() == other.area()

    def __notequal__(self, other):
        """Check if two squares have unequal areas.

        Args:
            other (Square): The other square to compare.
        """
        return self.area() != other.area()

    def __greaterthan__(self, other):
        """Check if the area of the current square is greater than the area of another square.

        Args:
            other (Square): The other square to compare.
        """
        return self.area() > other.area()

    def __GorE__(self, other):
        """Check if the area of the current square is greater than or equal to the area of another square.

        Args:
            other (Square): The other square to compare.
        """
        return self.area() >= other.area()

    def __lessthan__(self, other):
        """Check if the area of the current square is less than the area of another square.

        Args:
            other (Square): The other square to compare.
        """
        return self.area() < other.area()

    def __LorE__(self, other):
        """Check if the area of the current square is less than or equal to the area of another square.

        Args:
            other (Square): The other square to compare.
        """
        return self.area() <= other.area()
