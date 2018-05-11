
import pytest
from circle import *
import math


def test_r():
    c = Circle(4)
    assert c.radius == 4


def test_d():
    c = Circle(4)
    assert c.diameter == 8


def test_diameter_setting():
    c = Circle(4)
    c.diameter = 6
    assert c.diameter == 6
    assert c.radius == 3

def test_area():
    c = Circle(4)
    area = math.pi * 4 ** 2
    assert area == c.area
    try: c.area = 56
    except AttributeError:
        pass

def test_from_diameter():
    c = Circle.from_diameter(8)
    area = math.pi * 4 ** 2
    assert c.radius == 4
    assert c.diameter == 8
    assert area == c.area

def test_print():
    c = Circle(4)
    result = str(c)
    assert result == 'Circle with radius: 4.000000'

def test_prep():
    c = Circle(4)
    assert repr(c) == 'Circle(4)'

def test_add():
    c1 = Circle(2)
    c2 = Circle(4)
    print(c1 + c2)
    assert c1 + c2 == Circle(6)

def test_mul():
    c1 = Circle(3)
    n = 3
    assert c1 * n == Circle(9)
    assert n * c1 == Circle(9)

def test_comparison():
    c1 = Circle(5)
    c2 = Circle(9)
    c3 = Circle(9)
    assert c1 < c2
    assert c3 == c2

def test_sort():
    circles = [Circle(8), Circle(2), Circle(11), Circle(5), Circle(1), Circle(7), Circle(22)]
    circles.sort()
    assert circles == [Circle(1), Circle(2), Circle(5), Circle(7), Circle(8), Circle(11), Circle(22)]
