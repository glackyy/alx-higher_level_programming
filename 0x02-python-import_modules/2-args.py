#!/usr/bin/python3
import sys
if __name__ == "__main__":
    if len(sys.argv) > 0:
        print("{} arguments:".format(len(sys.argv)))
        for i in range(1, len(sys.argv) + 1):
            print("{}: {}".format(i, sys.argv[i - 1]))
