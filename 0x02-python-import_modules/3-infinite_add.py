#!/usr/bin/python3
from sys import argv
argv = argv[1:]
result = 0
if __name__ == "__main__":
    for num in argv:
        num = int(num)
        result += num
    print("{}".format(result))
