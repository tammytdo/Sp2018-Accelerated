#!/usr/bin/env python3

"""
Jay Johnson
circle
/////

# """
# Goal:
# The goal is to create a class that represents a simple circle.
#
# A Circle can be defined by either specifying the radius or the diameter, and the user can query the circle for either its radius or diameter.
#
# Other abilities of a Circle instance:
#
# Compute the circle’s area
# Print the circle and get something nice
# Be able to add two circles together
# Be able to compare two circles to see which is bigger
# Be able to compare to see if there are equal
# (follows from above) be able to put them in a list and sort them
# You will use:
# properties
# a classmethod
# define a bunch of “special methods”
# General Instructions:
# For each step, write a couple of unit tests that test the new features.
# Run these tests (and they will fail the first time)
# Add the code required for your tests to pass.
'''
class Circle(self=0):
    @staticmethod
    def radius(self):
        return print(self)

c = Circle(the_radius=4)
print(c.radius)
'''


class Circle(object):

    the_radius = 0

    def __init__(self, radius):
        self.radius = radius

    def radius_meth(self, radius):
        print(radius)


c = Circle(4)
print(c.radius)
