# -*- coding: utf-8 -*-
"""
Created on Sun May  6 14:45:38 2018

@author: mattn
"""

from circle.py import *


def test_radius():
    c = Circle(4)
    assert c.radius == 4
    
def test_diameter():
    c = Circle(4)
    assert c.diameter == 8
    
def test_area():
    c = Circle(4)
    assert c.area == str(50.26548245743669)
    if AssertionError:
        pass

