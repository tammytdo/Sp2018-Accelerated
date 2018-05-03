#!/usr/bin/env python
"""
Given two int values, return their sum. Unless the two values are the same, then return double their sum.
"""

from sum_double import sum_double


def test_1():
    assert sum_double(1, 2) is 3


def test_2():
    assert sum_double(3, 2) is 5


def test_3():
    assert sum_double(2, 2) is 8


def test_4():
    assert sum_double(-1, 0) is -1


def test_5():
    assert sum_double(3, 3) is 12


def test_6():
    assert sum_double(0, 0) is 0


def test_7():
    assert sum_double(0, 1) is 1


def test_8():
    assert sum_double(3, 4) is 7
