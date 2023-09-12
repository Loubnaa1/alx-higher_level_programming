#!/usr/bin/python3
"""contains function that writes a string to a text file"""


def write_file(filename="", text=""):
    """function that write to a file"""
    with open(filename, "w") as f:
        return f.write(text)
