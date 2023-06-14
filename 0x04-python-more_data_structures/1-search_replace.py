#!/usr/bin/python3
def search_replace(my_list, search, replace):
    res = []
    for e in my_list:
        if e == search:
            res.append(replace)
        else:
            res.append(e)
    return res
