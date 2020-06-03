#!/usr/bin/python3
""" a simple script that handle a files"""


def write_file(filename="", text=""):
    """ writes a string to a text file (UTF8) and returns the number
     of characters written"""
    with open(filename, 'w+',  encoding='utf-8') as fl:
        return fl.write(text)
