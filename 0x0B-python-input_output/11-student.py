#!/usr/bin/python3
""" a simple script that create a json from input"""


class Student:
    """that defines a student by"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """that retrieves a dictionary representation
                of a Student instance"""
        return {'first_name': self.first_name,
                'last_name': self.last_name,
                'age': self.age}
