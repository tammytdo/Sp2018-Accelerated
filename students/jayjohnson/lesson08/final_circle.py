#!/usr/bin/env python

import random
import time
import math


class Circle:
    '''
    Jay Johnson - Circle assignment - 5/7/2018
    The goal is to create a class that represents a simple circle.
    A Circle can be defined by either specifying the radius or the diameter, and the user can query the circle for either its radius or diameter.
    Other abilities of a Circle instance:

    Compute the circle’s area
    Print the circle and get something nice
    Be able to add two circles together
    Be able to compare two circles to see which is bigger
    Be able to compare to see if there are equal
    (follows from above) be able to put them in a list and sort them
    '''
    def __init__(self, the_radius):
        # STEP 1 The radius is a required parameter (can’t have a circle without one!)
        self.radius = the_radius
        # STEP 2 Add a “diameter” property, so the user can get the diameter of the circle:
        self.diameter = 2 *the_radius
        #Step 3 Set up the diameter property so that the user can set the diameter of the circle:
        # NEED TO FIGURE THIS OUT

        # Step 4 Add an area property so the user can get the area of the circle:
        self.area = math.pi * the_radius**2

    # step 5 Add an “alternate constructor” that lets the user create a Circle directly with the diameter:
    # def from_diameter(self, x):
    #     self.diameter = x
    #     self.radius = x / 2

    #STEP 6 Add __str__ and __repr__ methods to your Circle class.
    def __str__(self):
        return "Circle with a radius: " + str(self.radius)

    def __repr__(self):
        return "Circle(" + str(self.radius) + ")"

    def __add__(self, other):
        c1 = self.radius
        c2 = other.radius
        return "Circle(" + str(c1 + c2) + ")"

    def __lt__(self, other):
        c1 = self.radius
        c2 = other.radius
        return c1 < c2

    def __gt__(self, other):
        c1 = self.radius
        c2 = other.radius
        return c1 > c2

    def __eq__(self, other):
        c1 = self.radius
        c2 = other.radius
        return c1 == c2


if __name__ == '__main__':
    # f = Fraction(1, 0)  # ZeroDivisionError
    # f = Fraction(1.0, 2)    # TypeError
    # f1 = Fraction(1, 2)  # 1/2
    # print(f1)
    c = Circle(4)
    #STEP 1
    print(c.radius)

    #STEP 2
    print(c.diameter)

    #STEP 3
    c.diameter = 2
    print(c.diameter)
    print(c.radius)

    #STEP 4
    c = Circle(2)
    print(c.area)

    #STEP 5
    # c = Circle.from_diameter(8)
    # print(c.diameter)
    # print(c.radius)

    #STEP 6
    c = Circle(4)
    print(c)

    print(repr(c))

    c1 = Circle(2)
    c2 = Circle(4)

    #Step 7
    print(c1 + c2)
    #print(c2 * 3)

    #STEP 8
    print(c1 > c2)
    print(c1 < c2)
    print(c1 == c2)
    c3 = Circle(4)
    print(c2 == c3)
