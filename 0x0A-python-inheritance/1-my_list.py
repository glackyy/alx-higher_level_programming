#!/usr/bin/python3

"""Defining a class MyList"""


class Mylist(list):
    """Custom list class that inherits from list

    Methods: print_sorted()
    """

    def print_sorted(self):
        """Prints the list in sorted"""
        sorted_l = sorted(self)
        print(sorted_l)
