#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    dif_set = set()
    for e in set_1:
        if e not in set_2:
            dif_set.add(e)
    for e in set_2:
        if e not in set_1:
            dif_set_add(e)
    return dif_set
