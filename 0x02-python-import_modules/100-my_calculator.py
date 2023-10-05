#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    import sys
    from calculator_1 import add, sub, div, mul
    argv = argv[1:]
    length = len(argv)
    if length != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        a = int(argv[0])
        b = int(argv[2])
        sign = argv[1]
        if sign == "+":
            print("{} + {} = {}".format(a, b, add(a, b)))
        elif sign == "-":
            print("{} - {} = {}".format(a, b, sub(a, b)))
        elif sign == "/":
            print("{} / {} = {}".format(a, b, div(a, b)))
        elif sign == "*":
            print("{} * {} = {}".format(a, b, mul(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
