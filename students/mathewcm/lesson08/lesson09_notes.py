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

# What happens when yopu initalize a D object

d = D()

# without super() at all --  calling each subclass method explicitly 

class A():
    def this(self):
        print("in A.this")
        
class B():
    def this(self):
        print("in B.this")
        
class C(A,B):
    def this(self):
        A.this(self)
        B.this(self)

print("Running with super()")
c = C()
c.this()

#### Using super in just C

##### Explicity calling subclass methods gets tedious -- let's use super()


class A():
        def this(self):
            print("in A.this")
            
class B(A):
    def this(self):
        print("in B.this")
        
class C(B):
    def this(self):
        print("in C.this")
        super().this()
        
for c in C.__mro__:
    print(c)
    
class Base():
    def this(self):
        pass # just so there is a base that has the method
    
class A(Base):
    def this(self):
        print("in A.this")
        super().this()

class B(Base):
    def this(self):
        print("in B.this")
        super().this()

class C(A,B):
    def this(self):
        print("in C.this")
        super().this()
        
c = C()
c.this()
print(Base.__mro__)

#### Adding Up Immutables
import random

list_of_numbers = [random.randint(0, 100) for i in range(20)]
list_of_strings = ["this ", "that, ", "the other"]

def add_up_seq(seq, start=0):
    total = 0
    for item in seq:
        total += item
    return total

def make_really_big_string(n):
    s + ""
    for i in range(n):
        s += "a medium sized string"
        
