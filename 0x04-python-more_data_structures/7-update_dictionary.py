#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    for a_key in a_dictionary:
        if a_key is key:
            a_dictionary[a_key] = value
            return a_dictionary
    a_dictionary.update({key: value})
    return a_dictionary
