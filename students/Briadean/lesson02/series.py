#!/usr/bin/env python

def fibonacci(n):
    """A function to compute the Fibonacci series and return the nth value of the series """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def lucas(n):
    """A function to compute the Lucas series and return the nth value of the series"""
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)


def sum_series(n, a=0, b=1):
    """A generalized function to return the nth value of the Fibonnaci series by default, the lucas series when
    given the optional parameters a=2, b=1 and the nth value of any series based on this formula when given any
    other optional parameters."""
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        return sum_series(n - 1, a, b) + sum_series(n - 2, a, b)


# Assert statement to demonstrate correct fibonacci series values are returned by the given "nth" parameter
assert sum_series(4) == 3
# Assert statement to demonstrate correct lucas series values are returned by the given "nth" parameter
assert sum_series(9, a=2, b=1) == 76

if __name__ == "__main__":

    print(fibonacci(9))
    print(lucas(4))
    print(sum_series(4, a=4, b=2))
