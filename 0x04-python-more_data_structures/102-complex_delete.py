#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    list_key = list(a_dictionary.keys())
    for i in list_key:
        if a_dictionary[i] is value:
            a_dictionary.pop(i)
    return a_dictionary
