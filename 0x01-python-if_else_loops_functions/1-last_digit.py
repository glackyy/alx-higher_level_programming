#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastd = abs(number) % 10
if number < 0
    lastd = -lastd
print("Last digit of {} is {} and is".format(number, lastd), end=" ")
if lastd > 5:
    print("greater than 5")
elif lastd == 0:
    print("0")
else:
    print("less than 6 and not 0")
