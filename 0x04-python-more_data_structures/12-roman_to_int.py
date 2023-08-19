#!/usr/bin/python3

def roman_to_int(roman_string):
    somme = 0
    numb = 0
    dictionary = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    if not isinstance(roman_string, str):
        return 0
    index = len(roman_string) - 1
    while index >= 0:
        i = roman_string[index]
        numb = dictionary[i]
        if somme < numb * 5:
            somme += numb
        else:
            somme -= numb
        index -= 1    
    return somme
