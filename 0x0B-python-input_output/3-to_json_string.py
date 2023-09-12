#!/usr/bin/python3
"""contains function that returns the JSON representation"""
import json


def to_json_string(my_obj):
    """ function that returns the JSON representation"""
    return json.dumps(my_obj)
