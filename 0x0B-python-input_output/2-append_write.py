#!/usr/bin/python3
"""contains function that appends a string at
the end of a text file """


def append_write(filename="", text=""):
    """function that writes a string to a text file"""
    with open(filename, 'a') as f:
        return f.write(text)
