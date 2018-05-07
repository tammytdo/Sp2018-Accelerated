# -*- coding: utf-8 -*-
"""
Created on Sat May  5 15:14:49 2018

@author: mattn
"""

# UWPCE Circle Excercise

import math

class Circle:
    'An advanced circle analytic toolkit'
    
    version = '0.1'      # class variable
    
    def __init__(self, a_radius):
        self.radius = a_radius
        self.diameter = a_radius * 2
        
    def __str__(self):
        return f'Circle with radius: {c.radius:.6f}'
    
    
    def __repr__(self):
        return str(c)
    
    def __lt__(self):
        pass
    
    def __add__(self, other):
        c3 = c1 + c2
        
    
    def __mul__(self, other):
        pass
    
    @property
    def area(self):
        'Perform quadrature on a shape of uniform radius'
        return math.pi * self.radius ** 2.0


c = Circle(3)
# print(c.radius)
# print(c.diameter)

# a = Circle(4)
# print(str(math.pi * 4 ** 2.0))

def from_diameter():
    a_diameter = input('Enter a diameter and I will calulate the                         area for you ==> ')
    
from_diameter()   
print(c.area)

print(c)
    
c1 = Circle(2)
c2 = Circle(4)



    

    





