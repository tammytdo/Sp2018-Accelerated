#!/usr/bin3/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  5 15:14:49 2018
@author: mattn
"""

# UWPCE Circle Excercise

import math

class Circle():
    'An advanced circle analytic toolkit'
    
    version = '0.1'      # class variable
    
    def __init__(self, a_radius = None):
        if a_radius is None:
            self.radius = 0
        else:
            self.radius = a_radius
        
    def __str__(self):
        return 'Circle with radius: %d' % (self.radius)
    
    def __repr__(self):
        return 'Circle(%d)' % (self.radius)
    
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

    def __add__(self, other):
        return Circle(self.radius + other.radius)
        
    
    def __mul__(self, other):
        return Circle(self.radius * other)
    
    __rmul__ = __mul__
       
    @property
    def area(self):
        'Perform quadrature on a shape of uniform radius'
        return math.pi * self.radius**2
    
    @property
    def diameter(self):
        return 2 * self.radius
    @diameter.setter
    def diameter(self, val):
        self.radius = val / 2

    @classmethod
    def from_diameter(cls, diameter_value):
        self = cls(int(diameter_value / 2))
        return self




    

    





