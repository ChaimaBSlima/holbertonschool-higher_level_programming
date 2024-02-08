#!/usr/bin/python3
""" task 3: 3. Same class or inherit from"""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance or inherited of a class.

    Args:
        obj (any): The object to check.
        a_class (type): The class.
    Returns:
        If  is an instance - True.
        Otherwise - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
