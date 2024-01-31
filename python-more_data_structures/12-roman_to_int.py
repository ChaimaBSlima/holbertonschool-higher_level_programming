#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return (0)
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    a = 0
    for i in roman_string[::-1]:
        a = roman[i]
        if result < a * 5:
            result += a
        else:
            result -= a
    return (result)
