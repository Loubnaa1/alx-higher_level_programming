#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0

    total = 0
    digits = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    index = len(roman_string) - 1
    while index >= 0:
        r = roman_string[index]
        num = digits[r]
        if total < num * 5:
            total += num
        else:
            total -= num
        index -= 1

    return total
