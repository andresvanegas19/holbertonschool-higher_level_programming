#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for a_key in sorted(a_dictionary.keys()):
        print("{}: {}".format(a_key, a_dictionary.get(a_key)))
