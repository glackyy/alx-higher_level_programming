#!/usr/bin/python3
"""Defining class_to_json function"""


def class_to_json(obj):
    """Returns the dict description of the obj for JSON serialization

    Args:
        obj: An instance of a class
    """
    json_dic = {}
    for attrib in obj.__dict__:
        val = getattr(obj, attrib)
        if isinstance(val, (list, dict, str, int, bool)):
            json_dic[attrib] = val
    return json_dic
