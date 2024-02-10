#!/usr/bin/python3
"""Task 0: 0. Read file"""


def read_file(filename=""):
    """a function that reads a text file (UTF8) and prints it to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
