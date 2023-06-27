#!/usr/bin/python3

"""Define a Square."""


class Square:
    """Represents a Square."""

    def __init__(self, size=0, position=(0,0)):
        """Initialize a Square instance.

        Args:
            size (int): the size of the square.
            position (tuple): the position of the square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter/Setter of the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter/setter of the current position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(num, int) for num in value) or \
                not all(num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns The area of the square."""
        return self.size ** 2

    def my_print(self):
        """Print the square using the "#" character and pos."""
        if self.size == 0:
            print()
        else:
            for _ in range(self.position[1]):
                print()
            for _ in range(self.size):
                print(" " * self.position[0] + "#" * self.size)

