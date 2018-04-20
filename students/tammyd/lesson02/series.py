"""Fibonacci Sequece & Lucas Numbers"""

""" This program returns the nth number in the Fibonacci sequence. From Wikipedia: In mathematics, the Fibonacci numbers are the numbers in the following integer sequence, called the Fibonacci sequence, and characterized by the fact that every number after the first two is the sum of the two preceding ones. The first two Fibonacci numbers are 0 and 1."""

"""
def fibonacci(n):
    a,b = 0, 1
    for i in range(n-1):
        a,b = b, a+b
    return a

print("Fibonacci Sequence:")
for i in range(1,30):
    print(fibonacci(i))

print ("\n")

"""

"""This program returns the nth number in the Lucas Numbers series. From Wikipedia: Each Lucas number is defined to be the sum of its two immediate previous terms, thereby forming a Fibonacci integer sequence. The first two Lucas numbers are 2 and 1."""

def lucas(n):
    a,b = 2, 1
    for i in range(n-1):
        a,b = b, a+b
    return a

print("Lucas Numbers:")
for i in range(1,30):
    print(lucas(i))


#I am having a hard time understanding this part. I will ask during class. 

"""This function called sum_series has one required parameter and two optional parameters. The required parameter determines which element in the series to print. The two optional parameters have default values of 0 and 1 and determine the first two values for the series to be produced."""
"""

def sum_series(required, *args, **kwargs):

    if x == 0 and y == 1:
        for i in range(1,10):
            print(fibonacci(i))
    elif x == 2 and y == 1:
        for i in range(1,10):
            print(lucas(i))
    else:
        for i in range(1,10):
            print(fibonacci(i))

"""

def sum_series(n, s0=None, s1=None):
    print("sum_series called:", n)
    if n == 0:
        return s0
    elif n == 1:
        return s1
    elif n == 2:
        return s0 + s1
    elif n == 3:
        return (s0 +s1) + s1
    else:
        return (sum_series(n-1, s0, s1) + sum_series(n-2, s0, s1))

def fib(n):
    return sum_series(n, 0, 1)

def lucas(n):
    return sum_series(n, 2, 1)

#fib
assert sum_series(0, 0, 1) == 2
assert sum_series(1, 0, 1) == 1
assert sum_series(5,0, 1) == 1364

assert fib(0) == 0
assert fib(1) == 1
assert fib(2) == 1
assert fib(3) == 2
assert fib(4) == 3


#lucas 
assert sum_series(0, 2, 1) == 2
assert sum_series(0, 2, 1) == 1
assert sum_series(15,2, 1) == 1364

assert lucas(15) == 1364

print("all asserts passed")

print(sum_series(15, 2, 1))
