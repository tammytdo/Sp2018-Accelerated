#!/usr/bin/env python3

"""
A class that represents a simple circl.
"""
import math

class Circle():

    def __init__(self, r):
        self.radius = r
        self._diameter = self.radius * 2
        self._area = math.pi * self.radius ** 2

    @property
    def diameter(self):
        return self._diameter
    @diameter.setter
    def diameter(self, value):
        self._diameter = value
        self.radius = self._diameter / 2

    @property
    def area(self):
        self._area = math.pi * self.radius**2
        return self._area

    @classmethod
    def from_diameter(cls, value = None):
        radius = value / 2
        return cls(radius)

    def __str__(self):
        return f'Circle with radius: {self.radius:.6f}'

    def __repr__(self):
        return f'Circle({self.radius})'

    def __eq__(self, other):
        return self.radius == other.radius

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __mul__(self, other):
        return Circle(self.radius * other)

    __rmul__ = __mul__

    def __lt__(self, other):
        return self.radius < other.radius
