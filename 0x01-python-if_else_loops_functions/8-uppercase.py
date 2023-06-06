#!/usr/bin/python3
def uppercase(str):
    upper_char = []
    for c in str:
        if "a" <= c <= "z":
            c = chr(ord(c) - 32)
        upper_char.append(c)
    res = "".join(upper_char)
    print("{}\n".format(res))
