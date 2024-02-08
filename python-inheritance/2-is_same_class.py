#!/usr/bin/python3
"""Task 2: a class-checking function."""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a given class.

    Args:
        obj (any): The object to check.
        a_class (type): The class.
    Returns:
        if it is a class - True.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False
