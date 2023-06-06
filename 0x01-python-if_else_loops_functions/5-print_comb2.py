#!/usr/bin/python3
Op = ""
for i in range(100):
    Op += "{:02d}".format(i)
    if i != 99:
        Op += ", "
print(Op)
