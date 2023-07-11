#!/usr/bin/python3
"""Defining from_json_string function"""
import json


def from_json_string(my_str):
    """This function returns an obj represented by a JSON string

    Args:
        my_str (str): The JSON string representing the obj
    """
    return json.loads(my_str)
