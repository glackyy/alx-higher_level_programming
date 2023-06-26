#!/bin/usr/python3
def safe_print_list_integers(my_list=[], x=0):
    c = 0
    try:
        i = 0
        while True:
            try:
                val = my_list[i]
            except IndexError:
                break
            try:
                print("{:d}".format(val), end="")
                c += 1
            except ValueError:
                pass
            i += 1
            if c == x:
                break
    finally:
        print()
        return c
