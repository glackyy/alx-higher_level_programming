#!/usr/bin/python3
"""Defining an inherited list class MyList"""


class Mylist(list):
    """Custom list class that inherits from list."""

    def print_sorted(self):
        """Prints the list in sorted ascending order"""
        print(sorted(self))
