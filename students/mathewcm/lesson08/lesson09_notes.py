# -*- coding: utf-8 -*-
"""
Created on Mon May  7 15:16:25 2018

@author: mattn
"""

class A():
    def __init__(self):
        print("in A __init__ ")
        print("self's class is:", self.__class__)
        s = super().__init__()

class B():
    def __init__(self):
        print("in B __init__ ")
        print("self's class is:", self.__class__)
        s = super().__init__()
        
class C():
    def __init__(self):
        print("in C __init__ ")
        print("self's class is:", self.__class__)
        s = super().__init__()

class D(C, B, A):
    def __init__(self):
        print("in D.__init__")
        print("self's class is:", self.__class__)
        super().__init__()
        
# take a look at D's (M)ethod (R)esolution (O)rder:
print("D's MRO:")
for c in D.__mro__:
    print(c)


