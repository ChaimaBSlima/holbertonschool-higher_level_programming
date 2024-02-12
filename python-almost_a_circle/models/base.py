#!/usr/bin/python3
""" python-almost_a_circle project: Module for base """


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
