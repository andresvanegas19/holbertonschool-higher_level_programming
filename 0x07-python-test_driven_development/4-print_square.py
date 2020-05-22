#!/usr/bin/python3
"""Script to print a square
Attributes:
    size(int): is the size of the square
    if it fails raise a error
Example: ./4-main.py"""


def print_square(size):
    """print the a square
    :argument
        size(int): is the size of the square
    :return
        No return nothing"""
    if type(size) is not int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')

    for _ in range(size):
        for _ in range(size):
            print('#', end='')
        print(end='\n')
