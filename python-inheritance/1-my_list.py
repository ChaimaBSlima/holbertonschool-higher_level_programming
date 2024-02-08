#!/usr/bin/python3
""" task 1: Defines an inherited list class """


class MyList(list):
    """Implements sorted printing for the built-in list class."""

    def print_sorted(self):
        print(sorted(self))
