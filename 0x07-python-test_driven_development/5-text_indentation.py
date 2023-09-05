#!/usr/bin/python3
"""
containing a function that prints a text with two new lines after each '.','?' and ':'
"""


def text_indentation(text):
    """prints a text with two new lines after each '.','?' and ':'"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    while text[i] == ' ' and i < len(text):
        i += 1
    while i < len(text):
        print(text[i], end="")
        if text[i] == "\n" or text[i] in ".?:":
            if text[i] in ".?:":
                print("\n")
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1
