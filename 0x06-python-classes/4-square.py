#!/usr/bin/python3
"""define a Square"""

class Square:
    """represents a Square"""

    def __init__(self, size=0):
        """init instance of the class

        Args:
            size (int): The size of the new square
        """
        self.size = size
        
    @property
    def size(self):
        """Getter retrieving size of the square"""

        return self.__size

    @size.setter
    def size(self,value):
        """Setter for setting size of the square"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates area of the square.

        Returns:
            int: area of the square.
        """
        return self.__size ** 2
