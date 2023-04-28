#!/usr/bin/python3
"""MyList that inherits from list"""


class Mylist(list):
    """
    reps the class
    """
    def print_sorted(self):
        """
         prints the list, but sorted
        """
        print(sorted(self))
