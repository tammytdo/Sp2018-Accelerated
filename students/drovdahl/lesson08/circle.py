#! /usr/local/bin/python3
'''
Class that does the following:
    Compute the circle's area
    Print the circle and get something nice
    Add two circles together
    Compare two circles to see which is bigger
    Compare two circles to see if they are equal
    Put circles in a list and sort them

Use the following techniques
    properties
    classmethod
    special methods
'''
import math


class Circle(object):
    def __init__(self, radius):
        self._radius = radius
        self.diameter = radius * 2

    @property
    def radius(self):
        return self.diameter / 2

    @property
    def diameter(self):
        return self._radius * 2

    @diameter.setter
    def diameter(self, val):
        self._radius = val / 2

    @property
    def area(self):
        return math.pi * self._radius ** 2

    @classmethod
    def from_diameter(cls, diameter):
        self = cls(diameter/2)
        return self

    def __repr__(self):
        return 'Circle({})'.format(int(self._radius))

    def __str__(self):
        return 'Circle with radius: {:6f}'.format(self._radius)

    def __add__(self, other):
        return Circle(self._radius + other._radius)

    def __mul__(self, val):
        return Circle(self._radius * val)

    def __rmul__(self, val):
        return Circle(self._radius * val)

    def __gt__(self, other):
        return self._radius > other._radius

    def __lt__(self, other):
        return self._radius < other._radius

    def __eq__(self, other):
        return self._radius == other._radius


#if __name__ == '__main__':
    # c = Circle(10)
    # print('radius =', c.radius)
    # print('diameter =', c.diameter)
    # print('area =', c.area)
