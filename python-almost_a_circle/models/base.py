#!/usr/bin/python3
""" python-almost_a_circle project: Module for base
    starting at task 1
"""
from json import dumps


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
            return ("[]")
        else:
            return (dumps(list_dictionaries))
