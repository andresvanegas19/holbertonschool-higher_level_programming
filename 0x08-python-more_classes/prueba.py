#!/usr/bin/python3
""" Just a script that contains a class"""


class Rectangle:
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def __str__(self):
        return selfs.print_symbol


my_rectangle_1 = Rectangle(8, 4)
my_rectangle_1.print_symbol = "&"
print(my_rectangle_1.print_symbol)
print(my_rectangle_1)
