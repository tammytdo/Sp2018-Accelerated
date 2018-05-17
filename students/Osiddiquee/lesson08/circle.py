import math

class Circle:

    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def from_diameter(cls, diameter):
        radius = diameter / 2
        self = cls(radius)

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self._diameter = value
        self.radius = value / 2

    @property
    def area(self):
        return math.pi * self.radius**2

    def __str__(self):
        return f'Circle with radius: {self.radius}'

    def __repr__(self):
        return f'Circle({self.radius})'

    def __add__(self, other):
        return f'Circle({self.radius + other.radius})'

    def __mul__(self, number):
        return f'Circle({self.radius * number})'

    def __rmul__(self, number):
        return f'Circle({self.radius * number})'

    def __lt__(self, other):
        return self.radius < other.radius

    def __eq__(self, other):
        return self.radius == other.radius
