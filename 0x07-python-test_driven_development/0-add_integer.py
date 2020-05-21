#!/usr/bin/python3
"""Script to add two numbers
Attributes:
    add_integer (int): it return a integer if happen a wrong
    type or it passed a wrong type it will return a raise error
Example: ./0-main.py"""


def add_integer(a, b=98) -> int:
    """Add two numbers and return it
        a (int, float): The first parameter.
        b (str, float): The second parameter."""
    if a is None or type(a) not in [int, float]:
        raise TypeError('a must be an integer')
    if b is None or type(b) not in [int, float]:
        raise TypeError('b must be an integer')
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
