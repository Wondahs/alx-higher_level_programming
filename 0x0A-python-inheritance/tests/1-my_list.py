#!/usr/bin/python3
"""A class that inherits from lists"""


class MyList(list):
    """A class that inherits from lists"""

    def print_sorted(self):
        """Prints sorted list"""

        print(sorted(self))
