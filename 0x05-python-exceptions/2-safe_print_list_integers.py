#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    c = 0
    try:
        for i in range(0, x):
            try:
                val = my_list[i]
                if isinstance(val, int):
                    print("{:d}".format(my_list[i]),end="")
                    c += 1
            except (IndexError, TypeError):
                pass
    finally:
        print()
        return c
