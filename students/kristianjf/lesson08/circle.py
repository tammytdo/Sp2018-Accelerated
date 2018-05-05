#!/usr/bin/env python3
'Create a circle using classes'

'Create a circle using classes'

class Circle:
    def __init__(self, radius):
        self.radius = radius
    _diameter = None
    @property
    def diameter(self):
        self._diameter = self.radius * 2
        return self._diameter
    @diameter.setter
    def diameter(self, radius):
        self.radius = int(self._diameter / 2)
        return self.radius
