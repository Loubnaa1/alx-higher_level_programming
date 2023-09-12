#!/usr/bin/python3
"""contains function that returns the dictionary
representation of simple data structure
"""


def class_to_json(obj):
    """" returns the dictionary
    representation for JSON"""
    return obj.__dict__
