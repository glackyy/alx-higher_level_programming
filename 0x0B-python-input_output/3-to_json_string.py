#!/usr/bin/python3
"""Defining to_json_string function"""
import json


def to_json_string(my_obj):
    """This function returns the JSON representation of an obj

    Args:
        my_obj: The obj to be serialized into JSON
    """
    return json.dumps(my_obj)
