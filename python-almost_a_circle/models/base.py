#!/usr/bin/python3
""" python-almost_a_circle project: Module for base
    starting at task 1
"""
from json import dumps, loads


class Base:
    """ The base of ODP hierarchy """

    __nb_objects = 0

    def __init__(self, id=None):
        """ class constructor """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Task 15:  returns the JSON string
        representation of list_dictionaries
        """
        if list_dictionaries is None or not list_dictionaries:
            return ([])
        else:
            return (dumps(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """ Task 17: returns the list of the JSON
        string representation json_string
        """
        if json_string is None or not json_string:
            return ("[]")
        else:
            return (loads(json_string))

    @classmethod
    def save_to_file(cls, list_objs):
        "Task 16: saves jsonified object to file"
        if list_objs is not None:
            list_objs = [i.to_dictionary() for i in list_objs]
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_objs))
