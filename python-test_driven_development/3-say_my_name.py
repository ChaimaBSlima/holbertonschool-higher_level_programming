#!/usr/bin/python3
"""
This script defines a function 'say_my_name' that prints
the provided first name and last name.
If no last name is provided, it prints only the first name.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints the provided first name and last name.

    Parameters:
    - first_name (str): The first name to be printed.
    - last_name (str): The last name to be printed. Default is
    an empty string.

    Raises:
    - TypeError: If first_name or last_name is not a string.

    Returns:
    - None
    """

    # Check if first_name is a string
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    # Check if last_name is a string
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    # Print the name
    print("My name is {} {}".format(first_name, last_name))
