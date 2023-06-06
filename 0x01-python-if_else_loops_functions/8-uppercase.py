#!/usr/bin/python3
def uppercase(str):
    res = ""
    for c in str:
        if "a" <= c <= "z":
            c = chr(ord(c) - 32)
        res += c
    print(res)
