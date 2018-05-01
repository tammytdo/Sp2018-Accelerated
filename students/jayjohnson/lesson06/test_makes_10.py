#!/usr/bin/env python
"""
Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.
"""
from makes_10 import makes_10


def test_1():
    assert makes_10(9, 10) is True


def test_2():
    assert makes_10(9, 9) is False


def test_3():
    assert makes_10(1, 9) is True


def test_4():
    assert makes_10(10, 1) is True


def test_5():
    assert makes_10(10, 10) is True


def test_6():
    assert makes_10(8, 2) is True


def test_7():
    assert makes_10(8, 3) is False


def test_8():
    assert makes_10(10, 42) is True


def test_9():
    assert makes_10(12, -2) is True
