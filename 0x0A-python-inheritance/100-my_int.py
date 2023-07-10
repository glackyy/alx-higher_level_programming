#!/usr/bin/python3
"""Defining a class MyInt"""


class MyInt(int):
    """A class representing a rebel integer.Inherits from int"""

    def __eq__(self, other):
        """Override the equality comparison operator (==)

        Args:
            other: The object to compare with
        Returns:
            bool: True if the objects are not equal, False otherwise
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """Override the inequality comparison operator (!=)

        Args:
            other: The object to compare with
        Returns:
            bool: True if the objects are equal, False otherwise
        """
        return super().__eq__(other)
