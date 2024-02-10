#!/usr/bin/python3
"""Task 5: 5. Save Object to a file"""
import json


def save_to_json_file(my_obj, filename):
    """ a function that writes an Object to
    a text file, using a JSON representation"""
    with open(filename, "w") as chaima:
        json.dump(my_obj, chaima)
