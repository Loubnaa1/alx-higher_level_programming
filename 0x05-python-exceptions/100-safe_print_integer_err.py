#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except Exception as erreur:
        print("Exception: {}".format(erreur), file=sys.stderr)
        return False
