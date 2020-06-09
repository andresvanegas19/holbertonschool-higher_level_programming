#!/usr/bin/python3
"""This class will be the “base” of all other classes in this project.
The goal of it is to manage id attribute in all your future classes
and to avoid duplicating the same code (by extension, same bugs)"""
import csv
import json
from os import path


class Base:
    """This will be the base of everything"""
    __nb_objects = 0

    def __init__(self, id=None):
        if not id or id < 0:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """is a  the static method  that
        :return the JSON string representation of list_dictionaries"""
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        return '[]'

    @staticmethod
    def dict_return(list_objs):
        """ this function it will recive adress of classes
        :return the dictionary of those"""
        return [list_objs[i].to_dictionary()
                for i in range(len(list_objs))]

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file
        list_objs is a list of instances who inherits of Base"""
        # is a list of objects
        if not list_objs:
            with open(cls.__name__ + '.json', 'w') as flJson:
                flJson.write('[]')
                return
        real = cls.dict_return(list_objs)
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
        dummy = cls(1, 2)
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
        real = cls.dict_return(list_objs)
        with open(cls.__name__ + '.csv', 'w') as flCsv:
            # Opens the file so you can write it down
            writer = csv.writer(flCsv)
            try:
                # We tell him that the keys are going to make our columns
                writer.writerow(real[0].keys())
            except Exception as e:
                return
            for row in real:
                # Here we fill it with the rows
                writer.writerow(row.values())

    @classmethod
    def load_from_file_csv(cls):
        """This will load a csv file and become into json"""
        if not path.exists(cls.__name__ + '.json'):
            return []
        with open(cls.__name__ + '.csv') as fl:
            # Can't be done with the reader function
            # because it returns normal csv, it has to be manipulated with
            # Dict Readers
            inst = []
            for input_dict in csv.DictReader(fl):
                # load the file into dict
                real = json.loads(json.dumps(input_dict))
                # this is for become whole values into int
                for key, val in real.items():
                    real[key] = int(val)
                inst. append(cls.create(**real))
            return inst

    def draw(list_rectangles, list_squares):
        pass
