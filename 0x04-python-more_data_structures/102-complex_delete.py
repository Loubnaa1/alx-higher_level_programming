#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for i in list(a_dictionary.keys()):
        if a_dictionary[i] is value:
            a_dictionary.pop(list_key[i])
    return a_dictionary
