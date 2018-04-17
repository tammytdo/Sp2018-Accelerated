"""Fibonacci Sequece & Lucas Numbers"""

""" This program returns the nth number in the Fibonacci sequence. From Wikipedia: In mathematics, the Fibonacci numbers are the numbers in the following integer sequence, called the Fibonacci sequence, and characterized by the fact that every number after the first two is the sum of the two preceding ones. The first two Fibonacci numbers are 0 and 1."""

def fibonacci(n):
    a,b = 0, 1
    for i in range(n-1):
        a,b = b, a+b
    return a

print("Fibonacci Sequence:")
for i in range(1,30):
    print(fibonacci(i))

print ("\n")


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

sum_series()
