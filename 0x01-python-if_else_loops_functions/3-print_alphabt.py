#!/usr/bin/python3
for word in range(ord('a'),ord('z')+1):
    if ((word is not 113) and (word is not 101)):
        print("{:c}".format(word), end=" ")
