#!/usr/bin/python3
""" a simple script that handle a files"""


def read_lines(filename="", nb_lines=0):
    """ function that prints the lines of a text"""
    with open(filename, 'r',  encoding='utf-8') as fl:
        if nb_lines <= 0:
            print(fl.read())
            return
        else:
            count = 0
            for line in fl.readlines():
                count += 1
                if count > nb_lines:
                    return
                print(line, end='')
