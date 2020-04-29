#!/usr/bin/python3
def uppercase(words):
    for word in words:
        if ((ord(word) >= 97) and (ord(word) <= 122)):
            word = chr(ord(word) - 32)
        print("{}".format(word), end="")
    print("")
