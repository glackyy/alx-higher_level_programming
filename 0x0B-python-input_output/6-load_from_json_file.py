#!/usr/bin/python3
"""Defining load_from_json_file function"""
import json


def load_from_json_file(filename):
    """This function creates an obj from a JSON file

    Args:
        filename (str): The name of the json file
    Returns:
        obj: the Pyton obj created
    """
    with open(filename) as file:
        obj_data = json.load(file)
    return obj_data
