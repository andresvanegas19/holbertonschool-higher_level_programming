#!/usr/bin/python3
""" a simple script that handle a files"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file (UTF8) and
     returns the number of characters added:"""
    with open(filename, 'a', encoding='utf-8') as fl:
        return fl.write(text)
