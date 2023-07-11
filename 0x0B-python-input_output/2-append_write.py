#!/usr/bin/python3
"""Defining append_write function"""


def append_write(filename="", text=""):
    """This function appends a string at the end of a text file (UTF-8)

    Args:
        filename (str): The name of the file
        text (str): The string to be appended to the file
    Returns:
        The number of characters added to the file
    """
    with open(filename, mode='a', encoding='utf-8') as file:
        num_ch_added = file.write(text)
    return num_ch_added
