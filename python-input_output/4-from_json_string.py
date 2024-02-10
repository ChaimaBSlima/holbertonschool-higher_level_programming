#!/usr/bin/python3
"""Task 4: 4. From JSON string to Object"""
import json


def from_json_string(my_str):
    """a function that returns an object
    (Python data structure) represented by a JSON string"""
    return json.loads(my_str)
