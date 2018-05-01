#!/usr/bin/env python

"""
Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.
"""

def makes_10(a, b):
    if a == 10 or b == 10:
        return True
    if (a + b) == 10:
        return True
    else:
        return False
