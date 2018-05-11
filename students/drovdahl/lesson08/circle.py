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
        self.radius = radius
        self.diameter = radius * 2

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, val):
        self.radius = val / 2

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @classmethod
    def from_diameter(cls, diameter):
        self = cls(diameter/2)
        return self

    def __repr__(self):
        return 'Circle({})'.format(int(self.radius))

    def __str__(self):
        return 'Circle with radius: {:6f}'.format(self.radius)

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __mul__(self, val):
        return Circle(self.radius * val)

    def __rmul__(self, val):
        return Circle(self.radius * val)

    def __gt__(self, other):
        return self.radius > other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __eq__(self, other):
        return self.radius == other.radius


#if __name__ == '__main__':
    # c = Circle(10)
    # print('radius =', c.radius)
    # print('diameter =', c.diameter)
    # print('area =', c.area)
