#!/usr/bin/python3
def common_elements(set_1, set_2):
    common_set = set()
    for e in set_1:
        if e in set_2:
            common_set.add(e)
    return common_set
