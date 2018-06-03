import math

class Circle:
    """
    Class that represents the properties of a circle
    """
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("The radius of the circle can't be less than or equal to 0")
        else:
            self._radius = radius

    def __repr__(self):
        return 'Circle({})'.format(self.radius)

    def __str__(self):
        return 'Circle with radius: {}'.format(self.radius)  
    
    @property
    def radius(self):
        return self._radius
    @radius.setter
    def radius(self, val):
        if val <= 0:
            raise ValueError("The radius of the circle can't be less than or equal to 0")
        else:
            self._radius = val

    @property
    def diameter(self):
        return self.radius * 2
    @diameter.setter
    def diameter(self, val):
        self.radius = val / 2


    @property
    def area(self):
        """
        An area property so the user can get the area of the circle
        """
        return math.pi * (self.radius ** 2)

    @classmethod
    def from_diameter(cls, diameter):
        """
        An alternate constructor that lets the user create a Circle directly with the diameter
        """
        return cls(diameter / 2)

    # equality protocol for tests
    def __eq__(self, other):
        return self.radius == other.radius

    # Numeric Protocols
    # Add Circles
    # c1 = Circle(2)
    # c2 = Circle(4)
    # c1 + c2
    # Out[9]: Circle(6)
    # and multiply one times a number:
    # In [16]: c2 * 3
    # Out[16]: Circle(12)

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __mul__(self, other):
        return Circle(self.radius * other)

    def __rmul__(self, other):
        return Circle(self.radius * other)

    # Circle comparisons
    def __ne__(self, other):
        return self.radius != other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __le__(self, other):
        return self.radius <= other.radius


