#!/usr/bin/python3
def smiling(word, i):
    mayus = 0
    if word == 96:
        return 1
    else:
        if (i % 2 is 0):
            mayus = 32
        print(chr(word - mayus), end="")
#        print("{}".format(chr(word + mayus)), end="")
        return (smiling(word - 1,  i + 1))

smiling(122, 1)
