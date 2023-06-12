#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if isinstance(my_list, list):
        reversed_list = my_list[::-1]
        for item in reversed_list:
            if isinstance(item, int):
                print("{:d}".format(item))
