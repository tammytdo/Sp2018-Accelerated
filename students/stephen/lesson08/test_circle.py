import pytest
import math
from circle import Circle


def test_init():
    Circle(5)
    with pytest.raises(TypeError):
        Circle()
    with pytest.raises(ValueError):
        Circle(-5)
    with pytest.raises(ValueError):
        Circle(0)


def test_radius():
    c = Circle(4)
    assert c.radius == 4
    c.radius = 5
    assert c.radius == 5
    with pytest.raises(ValueError):
        c.radius = -5
    with pytest.raises(ValueError):
        c.radius = 0
    

def test_diameter():
    c = Circle(5)
    assert c.diameter == 10
    c.diameter = 20
    assert c.diameter == 20
    assert c.radius == 10
    with pytest.raises(ValueError):
        c.diameter = -10
    with pytest.raises(ValueError):
        c.diameter = 0

def test_area():
    c = Circle(5)
    assert c.area == (5 ** 2) * math.pi
    with pytest.raises(AttributeError):
        c.area = 36

def test_from_diameter():
    c = Circle.from_diameter(50)
    assert c.radius == 25
    assert c.diameter == 50
    assert c.area == (25 ** 2) * math.pi

def test_repr():
    c = Circle(9)
    assert repr(c) == 'Circle(9)'

def test_str():
    c = Circle(13)
    assert str(c) == 'Circle with radius: 13'

def test_add():
    c1 = Circle(5)
    c2 = Circle(2)
    assert (c1 + c2) == Circle(7)
    assert (c1 + c2) == (c2 + c1)

def test_mul():
    c1 = Circle(5)
    assert (c1 * 3) == Circle(15)
    assert (3 * c1) == Circle(15)
    assert (3 * c1) == (c1 * 3)

def test_comparisons():
    assert Circle(2) == Circle(4 / 2)
    assert Circle(2) > Circle(1)
    assert Circle(2) < Circle(3)
    assert Circle(2) <= Circle(2)
    assert Circle(2) <= Circle(3)
    assert Circle(2) >= Circle(2)
    assert Circle(2) >= Circle(1)

def test_sort():
    circles = [Circle(2), Circle(9), Circle(4), Circle(1)]
    assert sorted(circles) == [Circle(1), Circle(2), Circle(4), Circle(9)]