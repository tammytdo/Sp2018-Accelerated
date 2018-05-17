# -*- coding: utf-8 -*-
"""
Created on Sun May  6 14:45:38 2018

@author: mattn
"""

from circle import Circle

import pytest
import logging

def test_init():
    c = Circle()
    c = Circle(5)
    print(c)

def test_radius():
    c = Circle(5)
    assert c.radius == 5
    
def test_diameter():
    c = Circle(5)
    assert c.diameter == 10
    
def test_dia_chg():
    c1 = Circle(12)
    c1.diameter = 6
    
    assert c1.diameter == 6
    assert c1.radius == 3    
    
def test_area():
    logger = logging.getLogger(__name__)
    c = Circle(5)
    c1 = Circle(2)
    c2 = Circle(5)
    c3 = Circle(7)
    assert c.area == 78.53981633974483
    assert c1.area == 12.566370614359172
    assert c3.area == 153.93804002589985
    try:
        assert c2.area == 50.26548245743669
    except AssertionError as error:
        logger.error(AssertionError)
#        raise
#        raise AttributionError('assert 78.53981633974483 == 50.26548245743669 where          78.53981633974483 = Circle(5).area')
#        raise Exception()
        

def test_area_altcnstr():
    c1 = Circle.from_diameter(12)
    assert c1.diameter == 12
    assert c1.radius == 6
    
def test_str():
    c1 = Circle(4)
    d1 = str(c1)
    assert d1 == 'Circle with radius: 4'

def test_repr():
    c1 = Circle(5)
    d1 = repr(c1)
    assert d1 == 'Circle(5)'
    
def test_add():
    c1 = Circle(5)
    c2 = Circle(8)
    assert c1 + c2 == Circle(13)

def test_greater_than():
    c1 = Circle(9)
    c2 = Circle(7)
    c1_lt_c2 = c1 < c2
    c2_lt_c1 = c2 < c1
    assert c1_lt_c2 is False
    assert c2_lt_c1 is True
    

def test_less_than():
    c1 = Circle(7)
    c2 = Circle(9)
    c1_lt_c2 = c1 < c2
    c2_lt_c1 = c2 < c1
    assert c1_lt_c2 is True
    assert c2_lt_c1 is False

def test_eq_to():
    c1 = Circle(4)
    c2 = Circle(4)
    c3 = Circle(2)
    
    c1eqc2 = c1 == c2
    c1eqc3 = c1 == c3
    
    assert c1eqc2 is True
    assert c1eqc3 is False

def test_sort():
    circles = [Circle(7), Circle(3), Circle(4), Circle(9)]
    sorted_circles = sorted(circles)
    
    assert sorted_circles == [Circle(3), Circle(4), Circle(7), Circle(9)]
