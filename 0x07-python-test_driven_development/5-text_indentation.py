#!/usr/bin/python3
"""Script to contain a function prints with new space
Attributes:
    text_indentation(str): it print a new string
    recive an list with specific parameters
Example: ./5-main.py"""


def text_indentation(text):
    """divides all elements of a matrix.
    :argument
        text(str): is the text is going to print
    :return
        it will not return anything"""
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    verifier = True
    for num in range(len(text)):
        if not text[num] in ('.', ':', '?'):
            if verifier:
                print('{}'.format(text[num]), end='')
            verifier = True
        else:
            try:
                if text[num + 1] is ' ':
                    verifier = False
            except IndexError:
                pass
            print('{}'.format(text[num]), end='')
            print(end='\n\n')
