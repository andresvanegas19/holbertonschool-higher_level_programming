#!/usr/bin/python3
"""Script to print the two variables plus text
Attributes:
    first_name(str): the first name
    last_name(str): the second name
    if it fails raise a error
Example: ./3-main.py"""


def say_my_name(first_name, last_name=""):
    """print the arguments
        first_name(str): the first name
        last_name(str): the second name"""
    if type(first_name) is not str:
        raise TypeError('first_name must be a string')
    if type(last_name) is not str:
        raise TypeError('last_name must be a string')
    print('My name is {} {}'.format(first_name, last_name))
