import math


# Step 1
class Circle():
    def __init__(self, radius):
        self.radius = radius
        if self.radius < 0:
            raise ValueError("Radius can not be less than Zero")

# Step 2
    @property
    def diameter(self):
        return self.radius * 2

# Step 3
    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter / 2

# Step 4
    @property
    def area(self):
        return math.pi * (self.radius ** 2)

# Step 5
    # @classmethod
    # def from_diameter(cls, diameter):    FIX
    #     return cls.diameter

# Step 6
    def __str__(self):
        return "Circle with radius: {:6f}".format(self.radius)

    def __repr__(self):
        return "Circle({})".format(self.radius)

# Step 7
    def __add__(self, other):
        add_cir_rad = Circle(self.radius + other.radius)
        return eval(repr(add_cir_rad))

    def __mul__(self, multiplier):  # work on flipped multiplier
        mul_cir_rad = Circle(self.radius * multiplier)
        return eval(repr(mul_cir_rad))

# Step 8
    def __eq__(self, other):
        return self.radius == other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def sort_key(self):
        return self.radius  # siple sort by value no key given
