import math

class Circle:
    """
    Class that represents the properties of a circle
    """
    def __init__(self, the_radius):
        self._radius = the_radius
        self._diameter = 2 * the_radius
    
    @property
    def radius(self):
        return self._radius
    @radius.setter
    def radius(self, value):
        self._radius = value
        self._diameter = 2 * value

    @property
    def diameter(self):
        return self._diameter
    @diameter.setter
    def diameter(self, value):
        self._diameter = value
        self._radius = value / 2