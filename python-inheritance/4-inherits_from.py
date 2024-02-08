#!/usr/bin/python3
""" task 4: 4. Only sub class of"""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited instance of a class.

    Args:
        obj (any): The object to check.
        a_class (type): The class .
    Returns:
        Ifis an inherited instance of a_class - True.
        Otherwise - False.
    """
    if (issubclass(type(obj), a_class) and (type(obj) is not a_class)):
        return True
    return False
