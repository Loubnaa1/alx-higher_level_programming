#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0

    somme = 0
    dictionary = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    index = len(roman_string) - 1
    while index >= 0:
        i = roman_string[index]
        number = dictionary[i]
        if somme < number * 5:
            somme += number
        else:
            somme -= number
        index -= 1

    return somme
