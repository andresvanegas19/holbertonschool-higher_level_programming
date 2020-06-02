#!/usr/bin/python3
"""contains a simple function"""


def lookup(obj):
    """function that returns a list of available attributes and
    methods of an object
    :return a string"""
    return dir(obj)
