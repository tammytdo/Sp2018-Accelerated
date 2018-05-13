#!/usr/bin/env python3

import math

class Circle:

    def __init__(self, radius=0):
        self._radius = radius


    @property
    def radius(self):
        return self._radius


    @property
    def diameter(self):
        return (2 * self._radius)


    @property
    def area(self):
        return (self._radius * self._radius * math.pi)

    @classmethod
    def from_diameter(cls, diameter=0):
        circle1  = cls(diameter/2.0)
        return circle1


    def __str__(self):
        return "Circle with radius: {}".format(self._radius)


    def __repr__(self):
        return "Circle({})".format(self._radius)


    def __add__(self, other):
        return self._radius + other._radius


    def __gt__(self, other):
        return self._radius > other._radius


    def __lt__(self, other):
        return self._radius < other._radius


    def __ne__(self, other):
        return not (self._radius == other._radius)

    def __eq__(self, other):
        return self._radius == other._radius
