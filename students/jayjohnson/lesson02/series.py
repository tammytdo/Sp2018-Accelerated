'''
///////
Jay Johnson Fibonacci Series
///////
This program computes the nth term for the fibonacci and lucas series.  It will also sum these values together in another function.

Fibonacci and lucas series functions will take in a single value and give you the nth term of that valueself.

The sum function will take in a value for n and two optional values for the starting numbers of the lucas series.
///////

# notes
Step 1
x Create a new module series.py in the lesson02 folder in your student folder.
x In it, add a function called fibonacci.
x The function should have one parameter, n.
x The function should return the nth value in the fibonacci series.
Ensure that your function has a well-formed docstring
x Note that the fibinacci series is naturally recursive – the value is defined by previous values:

x fib(n) = fib(n-2) + fib(n-1)

x The Lucas Numbers (Links to an external site.)Links to an external site. are a related series of integers that start with the values 2 and 1 rather than 0 and 1. The resulting series looks like this:

2, 1, 3, 4, 7, 11, 18, 29, ...
x In your series.py module, add a new function, lucas, that returns the nth value in the lucas numbers series.

x Both the fibonacci series and the lucas numbers are based on an identical formula.

Add a third function called sum_series with one required parameter and two optional parameters. The required parameter will determine which element in the series to print.
The two optional parameters will have default values of 0 and 1 and will determine the first two values for the series to be produced.

Calling this function with no optional parameters will produce numbers from the fibonacci series.
Calling it with the optional arguments 2 and 1 will produce values from the lucas numbers. Other values for the optional parameters will produce other series.
Note: While you could check the input arguments, and then call one of the functions you wrote, the idea of this exercise is to make a general function, rather than one specialized.
So you should reimplement the code in this function.
In fact, you could go back and reimplement your fibonacci and lucas functions to call this one with particular arguments.
Ensure that your function has a well-formed docstring
Tests
Add a block of code to the end of your series.py module. Use the block to write a series of assertstatements that demonstrate that your three functions work properly.
Use comments in this block to inform the observer what your tests do.
Add your new module to your git clone and commit frequently while working on your implementation. Include good commit messages that explain concisely both what you are doing and why.
'''

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def lucas(n):
    if n == 0:
        return 2
    if n == 1:
        return 1
    return lucas(n - 1) + lucas(n - 2)

def sum_series(n,x=0,y=1):
    if x == 0 and y == 1:
        return fibonacci(n) + lucas(n)
    #else:
    #I could not get this portion working

#test block
print("This is each series counted out to the 7th term")
print("Fibonacci series:")
print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(4))
print(fibonacci(5))
print(fibonacci(6))
print(fibonacci(7))
print()

print("Lucas series:")
print(lucas(0))
print(lucas(1))
print(lucas(2))
print(lucas(3))
print(lucas(4))
print(lucas(5))
print(lucas(6))
print(lucas(7))
print()

print("This is each series summed together to the 7th term")
print(sum_series(0))
print(sum_series(1))
print(sum_series(2))
print(sum_series(3))
print(sum_series(4))
print(sum_series(5))
print(sum_series(6))
print(sum_series(7))
