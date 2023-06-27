#!/usr/bin/python3
"""define a Square"""


class Square:
    """represents a Square"""


    def __init__(self, size=0):
        """
        init instance of the class


        Args:
            size (int): The size of the new square
        """


        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """
        Calculates area of the square

        
        Returns:
               int: area of the square
        """

        return self.__size ** 2
