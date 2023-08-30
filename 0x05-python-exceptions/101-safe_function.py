#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        value = fct(*args)
        return value
    except Exception as erreur:
        print("Exception: {}".format(erreur), file=sys.stderr)
        return None
