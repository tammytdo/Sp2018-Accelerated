#! /usr/local/bin/python3


def fibonacci(n):
    '''
    This function will return the 'n'th value in the fibonacci series
    '''
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def lucas(n):
    '''
    This function returns the 'n'th value in the lucas series
    '''
    if n == 0:
        return 2
    if n == 1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)


def sum_series(n, a=0, b=1):
    '''
    This function determins which element in the series to print.
    The two optional parameters will have default values of 0 and 1 and
    will determine the first two values for the series to be produced.
    '''
#    print('a = ', a)
#    print('b = ', b)
    if n == 0:
        return a
    if n == 1:
        return b
    else:
        return sum_series(n-1, a, b) + sum_series(n-2, a, b)


print(fibonacci(10))
print(lucas(10))
print(sum_series(10, 2, 1))
