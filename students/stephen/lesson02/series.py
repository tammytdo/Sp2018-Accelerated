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
    if n == 1:
        return 2
    elif n == 2:
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)


print(lucas(4)) # should return 4 (2, 1, 3, 4, ...)

print(lucas(8)) # should return 29 (2, 1, 3, 4, 7, 11, 18, 29...)
    