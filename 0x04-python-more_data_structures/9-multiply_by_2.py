#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    multi_dict = {}
    for k, v in a_dictionary.items():
        multi_dict[k] = v * 2
    return multi_dict
