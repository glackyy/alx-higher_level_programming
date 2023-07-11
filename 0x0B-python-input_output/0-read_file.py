#!/usr/bin/python3
"""Defining a read_file function"""


def read_file(filename=""):
    """This function reads a text file (UTF8)
       and print the content to stdout

    Args:
        filename (str): the name of the file
    """
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end='')
