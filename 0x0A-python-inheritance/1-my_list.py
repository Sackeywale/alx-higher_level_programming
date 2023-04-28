#!/usr/bin/python3
"""MyList that inherits from list"""


class Mylist(list):
    """
        This class inherits from list.
        Attributes:
        Methods:
            print_sorted - prints the list in ascending order
    """
        def print_sorted(self):
            
    def print_sorted(self):
        """
         prints the list, but sorted
        """
        print(sorted(self))
