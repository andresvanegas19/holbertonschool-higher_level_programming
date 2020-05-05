#!/usr/bin/python3
def multiple_returns(sentence):
    if (not sentence):
        first_word = None
    else:
        first_word = sentence[0]
    lenght = len(sentence)
    new_tople = (lenght, first_word)
    return (new_tople)
