#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_ints = set()
    for e in my_list:
        if isinstance(e, int):
            uniq_ints.add(e)
    t = sum(uniq_ints)
    return t
