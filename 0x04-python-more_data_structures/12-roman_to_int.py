#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return (0)
    r_numerals = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
            }
    total = 0
    i = 0
    length = len(roman_string)
    while i < (length):
        if (roman_string[i] in r_numerals.keys()):
            if (i + 1) < len(roman_string):
                if (r_numerals[roman_string[i]] >=
                        r_numerals[roman_string[i + 1]]):
                    total += r_numerals[roman_string[i]]
                    i += 1
                    continue
                else:
                    total += (r_numerals[roman_string[i + 1]] -
                              r_numerals[roman_string[i]])
                    i += 2
                    continue
            else:
                total += r_numerals[roman_string[i]]
            i += 1
    return (total)
