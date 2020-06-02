#!/usr/bin/python3
""" a class that inherent from list"""


class MyList(list):
    """This classs inherent to list and
    carry whole atributes"""

    def print_sorted(self):
        """print the list of the inherent class
        in oreder"""
        print(sorted([a for a in super().__iter__()]))



