#!/usr/bin/python3
def uppercase(str):
    res = ""
    for c in str:
        if 97 <= ord(c) <= 122:
            upper_c = chr(ord(c) - 32)
            res += upper_c
        else:
            res += c
    print("{}\n".format(res), end="")
