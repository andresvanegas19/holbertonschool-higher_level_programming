#!/usr/bin/python3
""" a simple script that handle a files"""


def write_file(filename="", text=""):
    with open(filename, 'w+',  encoding='utf-8') as fl:
        return fl.write(text)
