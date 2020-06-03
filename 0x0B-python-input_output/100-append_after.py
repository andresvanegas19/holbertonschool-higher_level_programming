#!/usr/bin/python3
"""simple script that change the main file"""


def append_after(filename="", search_string="", new_string=""):
    """insert text in the exact position"""
    count = 0
    with open(filename, "r+") as f:
        text = f.readlines()
    for letter in text:
        count += 1
        if search_string in letter:
            text.insert(count, new_string)

    with open(filename, 'w') as f:
        f.write(''.join(text))
