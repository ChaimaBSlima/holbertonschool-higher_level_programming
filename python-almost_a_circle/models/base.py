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
            return ("[]")
        else:
            return (dumps(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """ Task 17: returns the list of the JSON
        string representation json_string
        """
        if json_string is None or not json_string:
            return ([])
        else:
            return (loads(json_string))

    @classmethod
    def save_to_file(cls, list_objs):
        "Task 16: saves jsonified object to file"
        if list_objs is not None:
            list_objs = [i.to_dictionary() for i in list_objs]
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_objs))

    @classmethod
    def create(cls, **dictionary):
        """ Task 18: Loads instance from dictionary """
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            chaima = Rectangle(1, 1)
        elif cls is Square:
            chaima = Square(1)
        else:
            chaima = None
        if chaima:
            chaima.update(**dictionary)
        return chaima

    @classmethod
    def load_from_file(cls):
        """ Task 19: Load string from a file and unjsonifies"""
        from os import path
        file = "{}.json".format(cls.__name__)
        if not path.isfile(file):
            return ([])
        with open(file, "r", encoding="utf-8") as f:
            return ([cls.create(**i) for i in cls.from_json_string(f.read())])
    
    @staticmethod
    def draw(list_rectangles, list_squares):
        import turtle
        import time
        from random import randrange
        turtle.Screen().colormode(255)
        for i in list_rectangles + list_squares:
            t = turtle.Turtle()
            t.color((randrange(255), randrange(255), randrange(255)))
            t.pensize(1)
            t.penup()
            t.pendown()
            t.setpos((i.x + t.pos()[0], i.y - t.pos()[1]))
            t.pensize(10)
            t.forward(i.width)
            t.left(90)
            t.forward(i.height)
            t.left(90)
            t.forward(i.width)
            t.left(90)
            t.forward(i.height)
            t.left(90)
            t.end_fill()

        time.sleep(5)
