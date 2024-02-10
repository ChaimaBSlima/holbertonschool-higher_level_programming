#!/usr/bin/python3
"""Task 10: 10. Student to JSON with filter"""


class Student:
    """
    a class Student that defines a student by: (based on 9-student.py)

    * Public instance attributes:
    first_name
    last_name
    age
    """

    def __init__(self, first_name, last_name, age):

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if (type(attrs) is list and
                all(type(i) is str for i in attrs)):
            return {j: getattr(self, j) for j in attrs if hasattr(self, j)}
        return self.__dict__
