#!/usr/bin/python3
"""Defining save_to_json_file function"""
import json


def save_to_json_file(my_obj, filename):
    """This function writes an obj to a text file

    Args:
        my_obj: The object to be serialized and written to the file
        filename (str): The name of the file
    """
    with open(filename, mode='w') as file:
        json.dump(my_obj, file)
