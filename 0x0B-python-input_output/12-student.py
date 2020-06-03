#!/usr/bin/python3
""" a simple script that create a json from input"""


class Student:
    """that defines a student by"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """that retrieves a dictionary representation
        of a Student instance"""
        att = {'first_name': self.first_name,
               'last_name': self.last_name,
               'age': self.age}
        if not attrs:
            return att
        search = {}
        for letter in attrs:
            try:
                search.update({letter: att[letter]})
            except Exception as e:
                pass
        return search
