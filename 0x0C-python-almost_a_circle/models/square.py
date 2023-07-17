#!/usr/bin/python3

"""Defining Square Class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from the Rectangle class

    Attributes:
        size (int): The size of the square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize the Square object

        Args:
            size (int): The size of the new Square
            x (int): The x coordinate of the new Square
            y (int): The y coordinate of the new Square
            id (int): id of the new Square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for the size attrib"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for the size attrib"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the attributes of the Square

        Args:
            *args: Variable number of arguments in the following order:
                - first argument: id attribute
                - second argument: size attribute
                - third argument: x attribute
                - fourth argument: y attribute
        """
        if args and len(args) != 0:
            attrs = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of the Square"""
        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }

    def __str__(self):
        """Returns a string representation of the Square"""
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y,
                                                 self.width)
