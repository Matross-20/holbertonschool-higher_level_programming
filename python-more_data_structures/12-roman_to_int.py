#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return 0

    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    total = 0
    i = 0

    while i < len(roman_string):
        if i + 1 < len(roman_string) and roman_values[roman_string[i]] < roman_values[roman_string[i + 1]]:
            total -= roman_values[roman_string[i]]
        else:
            total += roman_values[roman_string[i]]
        i += 1

    return total

