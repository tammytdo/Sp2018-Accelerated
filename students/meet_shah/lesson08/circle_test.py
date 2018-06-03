#!/usr/bin/env python3


from Circle import Circle
from math import *

c = Circle(2)
print(c.radius)
print(c.diameter)
print(c.area)

c1 = Circle.from_diameter(4)

print(c1)
print(repr(c1))

d = eval(repr(c))
print("here's d")
print(d)

c2 = Circle(2)
c3 = Circle(4)

print(c2 + c3)

print(c2 > c3)
print(c2 < c3)

print (c2 != c3)

circles = [Circle(6), Circle(7), Circle(8), Circle(4), Circle(0), Circle(2), Circle(3), Circle(5)]

print(circles)

circles.sort()
print(circles)
