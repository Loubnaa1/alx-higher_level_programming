#!/usr/bin/python3
"""containing a function called append_after"""


def append_after(filename="", search_string="", new_string=""):
    """function called append_after"""
    with open(filename, "r") as f:
        r_file = f.readlines()
    with open(filename, "w") as w:
        for line in r_file:
            w.write(line)
            if search_string in line:
                w.write(new_string)
