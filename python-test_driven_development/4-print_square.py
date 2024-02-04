#!/usr/bin/python3
"""
This script defines a function 'print_square' that prints a
square made of '#' characters with the specified size.
"""


def print_square(size):
    """
    Prints a square made of '#' characters with the specified size.

    Parameters:
    - size (int or float): The size of the square.

    Raises:
    - TypeError: If size is not an integer or if it's a negative float.

    Returns:
    - None
    """

    # Check if size is an integer or a non-negative float
    if not isinstance(size, (int, float)):
        raise TypeError("size must be an integer")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    # Check if size is non-negative
    if size < 0:
        raise TypeError("size must be >= 0")

    # Print the square
    for _ in range(int(size)):
        print("#" * int(size))
