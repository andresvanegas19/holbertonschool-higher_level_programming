#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return 0
    total = 0
    roman_numbers = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }
    for letter in roman_string:
        last_letter = letter
        for number in roman_numbers:
            if letter is number:
                total += roman_numbers[number]
    print(total)
    return 0
