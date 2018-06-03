import pytest
from Circle import Circle


def test_Circle_init():
    Circle(5)
    with pytest.raises(ValueError):
        Circle(-5)


def test_diameter():
    c1 = Circle(2)
    assert c1.diameter == 4


def test_area():
    c1 = Circle(1)
    assert c1.area == 3.141592653589793


def test_Circle_str():
    assert str(Circle(2)) == "Circle with radius: 2.000000"


def test_Circle_repr():
    assert repr(Circle(2)) == "Circle(2)"


def test_add_cir():
    add_cir_rad = Circle(2) + Circle(4)
    assert eval(repr(add_cir_rad)) == Circle(6)


def test_mult_cir():
    mult_cir_rad = Circle(2) * 4
    assert eval(repr(mult_cir_rad)) == Circle(8)


def test_cir_eq():
    c1 = Circle(2)
    c2 = Circle(2)
    assert c1.diameter == c2.diameter
    assert c1.radius == c2.radius
    assert c1.area == c2.area


def test_cir_lt():
    c1 = Circle(2)
    c2 = Circle(3)
    assert c1.diameter < c2.diameter
    assert c1.radius < c2.radius
    assert c1.area < c2.area


def test_cir_gt():
    c1 = Circle(3)
    c2 = Circle(2)
    assert c1.diameter > c2.diameter
    assert c1.radius > c2.radius
    assert c1.area > c2.area


def test_sort_key():
    circles = [Circle(6), Circle(7), Circle(8), Circle(4), Circle(0),
               Circle(2), Circle(3), Circle(5), Circle(9), Circle(1)]
    circles.sort() == [Circle(0), Circle(1), Circle(2), Circle(3), Circle(4),
                       Circle(5), Circle(6), Circle(7), Circle(8), Circle(9)]
