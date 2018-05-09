'''
This is the test program for circle.py
'''
from circle import *

def test_init():
    c = Circle(5)
    assert c.radius == 5
    assert c.diameter == 10


def test_change_diameter():
    c = Circle(5)
    c.diameter = 8
    assert c.radius == 4


def test_area():
    c = Circle(2)
    assert round(c.area, 2) == 12.57


def test_alternate_constructor():
    c = Circle.from_diameter(8)
    assert c.diameter == 8
    assert c.radius == 4


def test_str():
    c = Circle(4)
    print(c)


def test_repr():
    c = Circle(4)
    repr(c)


def test_numeric():
    c1 = Circle(2)
    c2 = Circle(4)

    assert c1 + c2 == 'Circle(6)'
    c2 * 3 == 'Circle(12)'
    3 * c2 == 'Circle(12)'

def test_sort():
    l = [Circle(4), Circle(2), Circle(6)]
    assert sorted(l) == [Circle(2), Circle(4), Circle(6)]
