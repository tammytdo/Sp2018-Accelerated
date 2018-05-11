"""
circles.py

this is the circles.py exercise from lesson #8

"""

import math


class Circle:

    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter / 2

    @property
    def area(self):
        return math.pi * self.radius**2

    def __str__(self):
        return f"Circle with radius: {self.radius}"

    def __repr__(self):
        return f"Circle ({self.radius})"

    def __eq__(self, other):
        return Circle(self.radius == other.radius)

    def __lt__(self, other):
        return Circle(self.radius > other.radius)

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __mul__(self, other):
        return Circle(self.radius * other.radius)


if __name__ == '__main__':

    c = Circle(2)

    print(c.radius)
    print(c.diameter)
    print(c.area)
