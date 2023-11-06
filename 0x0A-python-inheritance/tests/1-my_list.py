#!/usr/bin/python3
"""A class that inherits from lists"""


class MyList(list):
    """A class that inherits from lists"""

    def __init__(self, *args):
        super().__init__(*args)

    def print_sorted(self):
        """Prints sorted list"""

        print(sorted(self))
