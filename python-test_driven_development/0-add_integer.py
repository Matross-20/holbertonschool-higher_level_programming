#!/usr/bin/python3
""" 0-add_integers.py """


def add_integer(a, b=98):
    """
    Adds two numbers

    args:
        a = first number
        b = second number

    Returns:
        sum of two numbers

    """

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
