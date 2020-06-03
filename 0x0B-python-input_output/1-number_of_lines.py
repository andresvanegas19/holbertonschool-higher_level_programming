#!/usr/bin/python3
""" a simple script that handle a files"""


def number_of_lines(filename=""):
    with open(filename, 'r',  encoding='utf-8') as fl:
        return len(fl.readlines())
