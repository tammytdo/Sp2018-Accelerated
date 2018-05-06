import math

class Circle():

    def __init__(self, r = None):

        if r is None:
            self.radius = 0
        else:
            self.radius = r

    def __str__(self):
        return 'Circle with radius: %d' % (self.radius)

    def __repr__(self):
        return 'Circle(%d)' % (self.radius)

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __mul__(self, other):
        return Circle(self.radius * other)

    # def __rmul__(self, other):
    #     return Circle(self.radius * other)
    __rmul__ = __mul__

    def __gt__(self, other):
        if self.radius > other.radius:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.radius < other.radius:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.radius == other.radius:
            return True
        else:
            return False

    @property
    def diameter(self):
        return 2 * self.radius
    @diameter.setter
    def diameter(self, val):
        self.radius = val / 2

    @property
    def area(self):
        return math.pi * self.radius**2

    @classmethod
    def from_diameter(class_object, d = None):
        return class_object(d / 2)
