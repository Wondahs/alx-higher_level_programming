#!/usr/bin/python3
import hidden_4
module_name = dir(hidden_4)
names = [name for name in module_name if not name.startswith('_')]
if __name__ == "__main__":
    for name in names:
        print("{}".format(name))
