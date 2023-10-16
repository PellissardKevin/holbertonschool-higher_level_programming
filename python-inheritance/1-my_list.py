#!/usr/bin/python3
"""Definition of function my_list"""


class MyList(list):
    """Class Mylist with list in inherit"""

    def print_sorted(self):
        """"Function that prints the list, but sorted """
        print(sorted(self))
