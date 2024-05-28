"""Module to read a file from argument"""

def write_file(filename="", text=""):
    """Function to write file"""
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
