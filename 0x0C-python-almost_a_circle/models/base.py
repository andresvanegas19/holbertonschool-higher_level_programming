#!/usr/bin/python3
"""This class will be the “base” of all other classes in this project.
The goal of it is to manage id attribute in all your future classes
and to avoid duplicating the same code (by extension, same bugs)"""
import json
import models.rectangle as rect
from os import path
import csv


class Base:
    """This will be the base of everything"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """is a  the static method  that
        :return the JSON string representation of list_dictionaries"""
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        return '[]'

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file
        list_objs is a list of instances who inherits of Base"""
        # is a list of objects
        real = [list_objs[i].to_dictionary()
                for i in range(len(list_objs))]
        # open the file and write into it
        with open(cls.__name__ + '.json', 'w') as flJson:
            flJson.write(cls.to_json_string(real))

    @staticmethod
    def from_json_string(json_string):
        """that returns the list of the JSON string representation
        json_string, that returns a list of instances"""
        if json_string:
            # loads for read jsons
            return json.loads(json_string)
        return []

    @classmethod
    def create(cls, **dictionary):
        """To use the update method to assign all attributes, you must
        create a “dummy” instance before"""
        dummy = rect.Rectangle(0, 1, 0, 1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """:returns a list of instances"""
        if not path.exists(cls.__name__ + '.json'):
            return []
        with open(cls.__name__ + '.json', 'r') as flJson:
            # try to read the first character if is not possible
            # it will return False
            inst = []
            a = cls.from_json_string(flJson.read())
            for values in a:
                inst.append(cls.create(**values))
            return inst

    @classmethod
    def save_to_file_csv(cls, list_objs):
        pass

    @classmethod
    def load_from_file_csv(cls):
        pass
