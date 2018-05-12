#! /usr/local/bin/python3
'''
test code for circle.py
'''
from circle2 import *
import math


def test_radius():
    c = Circle(10)
    assert c.radius == 10


def test_diameter():
    c = Circle(2)
    assert c.diameter == 4


def test_radius_change():
    c = Circle(3)
    assert c.radius == 3
    c.radius = 4
    assert c.radius == 4


def test_diameter_change():
    c = Circle(4)
    assert c.diameter == 8
    c.diameter = 10
    assert c.radius == 5


def test_area():
    c = Circle(5)
    assert c.area == (math.pi * 25)
    while True:
        try:
            c.area = 1
        except AttributeError:
            break
        raise  # raise error if able to set area


def test_alternate_constructor():
    # uses classmethod to pass diameter to create circle list_of_simple_objects
    c = Circle.from_diameter(10)
    c.radius == 5
    c.diameter == 10


def test_repr_and_str():
    c = Circle(4)
    assert repr(c) == 'Circle(4)'
    assert str(c) == 'Circle with radius: 4.000000'


def test_addition():
    c1 = Circle(2)
    c2 = Circle(4)
    assert repr(c1 + c2) == 'Circle(6)'


def test_multiplication():
    c1 = Circle(4)
    assert repr(c1 * 3) == 'Circle(12)'


def test_multiplication2():
    c2 = Circle(2)
    assert repr(3 * c2) == 'Circle(6)'


def test_greater_than():
    c1 = Circle(10)
    c2 = Circle(20)
    assert (c2 > c1) is True
    assert (c1 > c2) is False


def test_less_than():
    c1 = Circle(1)
    c2 = Circle(2)
    assert (c1 < c2) is True
    assert (c2 < c1) is False


def test_equal():
    c1 = Circle(100)
    c2 = Circle(100)
    assert (c1 == c2) is True
    c2 = Circle(101)
    assert (c1 == c2) is False


def test_sort():
    c = [Circle(2), Circle(6), Circle(1), Circle(15), Circle(10)]
    assert (c[0] < c[1] < c[2] < c[3] < c[4]) is False
    c.sort()
    assert (c[0] < c[1] < c[2] < c[3] < c[4]) is True
