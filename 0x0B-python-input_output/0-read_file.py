#!/usr/bin/python3
""" a simple script of I/O"""


def read_file(filename=""):
    """is a function to print the content of  a file"""
    with open(filename, 'r', encoding='utf-8') as fl:
        print(fl.read())
