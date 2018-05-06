#!/usr/bin3/env python3

from circle import Circle

import pytest
import unittest


# Step 1:
def test_intialize():
    """
    Test that the radius gets initialized
    """
    c = Circle()
    c = Circle(4)


def test_radius():
    """
    Test that the radius is the radius
    """
    c = Circle(4)

    assert c.radius == 4


# Step 2:
def test_diameter():
    """
    Test that the diameter gets calculated properly
    """
    c = Circle(4)

    assert c.diameter == 8


# Step 3:
def test_diameter_param():
    """
    Test that the diameter property can be inputted, changing
    both the diameter and radius properties appropriately
    """

    c = Circle(4)
    c.diameter = 2

    assert c.diameter == 2
    assert c.radius == 1


# Step 4:
def test_area():
    """
    Test that the area gets calculated properly
    """
    c = Circle(4)

    assert c.area == 50.26548245743669

# Not sure how to test for errors...
# def test_area_param():

#     c = Circle(4)

#     with assertRaises(AttributeError):
#         c.area = 42


# Step 5: 
def test_alt_constructor():
    """
    Test that the alternate constructor of from_diameter() works.
    If the alternate constructor is used to create a Circle,
    radius should be updated accordingly.
    """
    c = Circle.from_diameter(4)

    assert c.diameter == 4
    assert c.radius == 2


# Step 6: 
def test_print():
    """
    Test that printing a Circle class object prints the string
    that is in __str__ 
    """
    c = Circle(4)
    s = str(c)

    assert s == "Circle with radius: 4"


# Step 7:
def test_add():
    """
    Test that adding two Circle classes together yields a
    Circle class with sums of their radii
    """
    c1 = Circle(2)
    c2 = Circle(4)

    assert c1 + c2 == Circle(6)


# Step 8:
def test_greater_than():
    """
    Test that the Circles can be compared with greater than statement
    """
    c1 = Circle(2)
    c2 = Circle(4)

    result1 = c1 > c2
    result2 = c2 > c1

    assert result1 is False
    assert result2 is True


def test_less_than():
    """
    Test that the Circles can be compared with less than statement
    """

    c1 = Circle(2)
    c2 = Circle(4)

    result1 = c1 < c2
    result2 = c2 < c1

    assert result1 is True
    assert result2 is False


def test_equal_to():
    """
    Test that the Circles can be compared to see if they're equal
    """
    c1 = Circle(4)
    c2 = Circle(4)
    c3 = Circle(2)

    result1 = c1 == c2
    result2 = c1 == c3

    assert result1 is True
    assert result2 is False


def test_list():
    """
    Test that a list of Circles gets sorted properly, according
    to its radius
    """

    circles = [Circle(2), Circle(4), Circle(1), Circle(3)]
    sorted_circles = sorted(circles)

    assert sorted_circles == [Circle(1), Circle(2), Circle(3), Circle(4)]


