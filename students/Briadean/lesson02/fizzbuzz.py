#!/usr/bin/env python

"""
A script which prints the numbers from 1 to 100 inclusive.

Multipliers of 3 are replaced with "Fizz", multipliers of 5
are replaced with "Buzz", and multipliers of 3 and 5 are replaced with "Fizzbuzz"
"""

for num in range(1, 100 + 1):
    if num % 3 ==0 and num % 5 == 0:
        print("Fizzbuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
