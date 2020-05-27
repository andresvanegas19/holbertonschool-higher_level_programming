#!/usr/bin/python3
"""script that protect
 that prevents the user from dynamically
 creating new instance attributes"""


class LockedClass:
    """ that prevents the user from dynamically
    creating new instance attributes"""

    def __init__(self, value):
        self.first_name = value
        self.__freeze()
