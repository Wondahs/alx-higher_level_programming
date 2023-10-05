#!/usr/bin/python3
from sys import argv
argv = argv[1:]
length = len(argv)
if __name__ == "__main__":
    if length < 2:
        print("{} argument{}".format(length, "." if length == 1 else "s."))
    else:
        print("{} arguments:".format(length))
    if length > 0:
        for index, value in enumerate(argv, start=1):
            print("{} : {}".format(index, value))
