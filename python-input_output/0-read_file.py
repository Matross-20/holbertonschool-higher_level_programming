#!/usr/bin/python3
"""Module to read a file from argument"""

def read_file(filename=""):
    """
    Reads a UTF-8 encoded text file and prints its content to stdout.

    Args:
        filename (str): The path to the file to be read. Default is an empty string.
    """
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
