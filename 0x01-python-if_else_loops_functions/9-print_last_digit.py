#!/usr/bin/python3
def print_last_digit(number):
    figure = number
    if number < 0:
        figure *= -1
    divisor = 10
    remainder = figure % divisor
    print(f"{remainder}", end='')
    return remainder
