# Lesson 02 Assignment: Series
# Step 1
# Create a new module series.py in the lesson02 folder in your student folder.
# In it, add a function called fibonacci.
# The function should have one parameter, n.
# The function should return the nth value in the fibonacci series.
# Ensure that your function has a well-formed docstring
# Note that the fibinacci series is naturally recursive – the value is defined by previous values:
# fib(n) = fib(n-2) + fib(n-1)

def fibonacci(n):
    """Return the nth value of the Fibonacci series"""
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(3)) # should return 1 (0, 1, 1, ...)

print(fibonacci(8)) # should return 13 (0, 1, 1, 2, 3, 5, 8, 13, ...)

# Step 2
# Lucas Numbers
# The Lucas Numbers are a related series of integers that start
# with the values 2 and 1 rather than 0 and 1. The resulting series looks like this:
# 2, 1, 3, 4, 7, 11, 18, 29, ...
# In your series.py module, add a new function, lucas, that returns the nth value in the lucas numbers series.
# Ensure that your function has a well-formed docstring.

def lucas(n):
    """Return the nth value of the Lucas series."""
    if n == 1:
        return 2
    elif n == 2:
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)


print(lucas(4)) # should return 4 (2, 1, 3, 4, ...)

print(lucas(8)) # should return 29 (2, 1, 3, 4, 7, 11, 18, 29...)

# Step 3
# Generalizing
# Both the fibonacci series and the lucas numbers are based on an identical formula.
# Add a third function called sum_series with one required parameter and two optional parameters.
# The required parameter will determine which element in the series to print. The two optional parameters
# will have default values of 0 and 1 and will determine the first two values for the series to be produced.

# Calling this function with no optional parameters will produce numbers from the fibonacci series.
# Calling it with the optional arguments 2 and 1 will produce values from the lucas numbers. Other values for
# the optional parameters will produce other series.

def sum_series(n, a = 0, b = 1):
    """
    Return the nth term of a series where every term is the sum of the previous two terms.
    The a and b parameters specify the first and second values, respectively, in the series.
    """
    if n == 1:
        return a
    elif n == 2:
        return b
    else:
        return sum_series(n - 1, a, b) + sum_series(n - 2, a, b)

# The following should print the same results as fibonacci(1) and fibonacci(8)
print(sum_series(3))
print(sum_series(8))
    
# The following should print the same results as lucas(4) and lucas(8)
print(sum_series(4, 2, 1))
print(sum_series(8, 2, 1))