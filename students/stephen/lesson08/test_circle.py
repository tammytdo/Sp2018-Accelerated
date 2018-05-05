import pytest
from circle import Circle

def test_radius():
    c = Circle(4)
    assert c.radius == 4

def test_diameter():
    c = Circle(5)
    assert c.diameter == 10