#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    res = sum(int(arg) for arg in args)
    print(res)
