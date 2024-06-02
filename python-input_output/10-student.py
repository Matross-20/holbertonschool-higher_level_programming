#!/usr/bin/python3
"""
9-student.py defines a student class
"""


class Student:
    """
    Defines a student

    Args:
        first_name (str): first name of student
        last_name (str): last name of student
        age (int): age of the student

    Attributes:
        first_name (str): first name of student
        last_name (str): last name of student
        age (int): age of the student
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance

        Returns:
            A dictionary representation of a Student instance
        """

        if attrs is not None:
            if all(isinstance(element, str) for element in attrs):
                filtered_dict = {}
                for attr in attrs:
                    if hasattr(self, attr):
                        filtered_dict[attr] = getattr(self, attr)
                return filtered_dict
        return self.__dict__
