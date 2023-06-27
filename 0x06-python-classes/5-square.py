#!/usr/bin/python3

"""Define a class Square."""

class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initialize a Square instance.

        Args:
            size (int): The size of the square.
        """
        self.size = size

    @property
    def size(self):
        """Getter/Setter the current size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns The area of the square."""
        return self.size ** 2

    def my_print(self):
        """Print the square using the '#' character."""
        if self.size == 0:
            print()
        else:
            for _ in range(self.size):
                print("#" * self.size)

