#!/usr/bin/python3

"""Defining a Rectangle class"""


class Rectangle:
    """Represents a rectangle

    Attributes:
        num_of_instances: (int)
    """

    num_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializing a new instance

        Args:
            width: (int)
            height: (int)
        """
        self.width = width
        self.height = height
        type(self).num_of_instances += 1

    @property
    def width(self):
        """Returns the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width

        Args:
            value: (int)
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the height

        Args:
            value: (int)
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates and Returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates and Returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns a string representing the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rec = []
        for i in range(self.__height):
            [rec.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rec.append("\n")
        return ("".join(rec))

    def __repr__(self):
        """Returns a string representing the rectangle"""
        rec = "Rectangle(" + str(self.__width)
        rec += ", " + str(self.__height) + ")"
        return rec

    def __del__(self):
        """Deletes rectangle"""
        type(self).num_of_instances -= 1
        print("Bye rectangle...")
