#!/usr/bin/python3

"""Defining Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class that inherits from the Base class

    Attributes:
        width (int): The width of the rectangle
        height (int): The height of the rectangle
        x (int): The x-coordinate of the rectangle's pos
        y (int): the y-coordinate of the rectangle's pos
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the Rectangle object

        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
            x (int): The x-coordinate of the rectangle's pos
            y (int): the y-coordinate of the rectangle's pos
            id (int): Unique id for the rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for the width attrib"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width attrib"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for the height attrib"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the height attrib"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for the x attrib"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for the x attrib"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for the y attrib"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for the y attrib"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of the Rectangle"""
        return self.width * self.height

    def display(self):
        """Print the Rectangle instance with "#"."""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def update(self, *args, **kwargs):
        """Update the attrib of the rectangle

        Args:
            *args: Variable num of args in the following order:
                first argument : id
                second argument: width
                third argument: height
                fourth argument: x
                fifth argument: y
        """
        if len(args) > 0:
            attrs = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        elif len(kwargs) > 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of the Rectangle"""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }

    def __str__(self):
        """Returns a string representation of the Rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)
