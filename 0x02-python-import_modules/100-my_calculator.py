#!/usr/bin/python3
if (__name__== "__main__"):
    import sys
    from calculator_1 import add,sub,mul,div
    if (len(sys.argv)) < 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(sys.argv[1])
    op = sys.argv[2]
    b = int(sys.argv[3])
    if (op == '+'):
        res = add(a, b)
    elif (op == '-'):
        res = sub(a, b)
    elif (op == '*'):
        res = mul(a, b)
    elif (op == '/'):
        res = div(a, b)
    else:
        print("Unknown operator, Available operators: +, -, * and /")
        sys.exit(1)
    print("{:d} {} {:d} = {:d}".format(a, op, b, res))
