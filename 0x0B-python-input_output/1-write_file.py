#!/usr/bin/python3
"""Defining write_file function"""


def write_file(filename="", text=""):
    """This function writes a string to a text file (UTF-8)

    Args:
        filename (str): The name of the file
        text (str): The string to be written to the file
    Returns:
           The number of characters written to the file
    """
    with open(filename, mode='w', encoding='utf-8')
        num_ch = file.write(text)
    return num_ch
