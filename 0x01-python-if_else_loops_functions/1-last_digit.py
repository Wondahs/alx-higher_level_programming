#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
figure = number
if number < 0:
    figure = number * (-1)
divisor = 10
remainder = figure % divisor
if number < 0:
    remainder = remainder * (-1)
if remainder > 5:
    print(f"Last digit of {number} is {remainder} and is greater than 5")
elif remainder == 0:
    print(f"Last digit of {number} is {remainder} and is 0")
elif remainder < 6 and not remainder == 0:
    print(f"Last digit of {number} is {remainder} "
          f"and is less than 6 and not 0")
