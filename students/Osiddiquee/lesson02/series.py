#nth parameter of fibonacci function
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

#nth parameter of lucas function
def lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)

#nth paramater of generalized series function
def sum_series(n, first = 0, second = 1):
    if n == 0:
        return first
    elif n == 1:
        return second
    else:
        return sum_series(n-1, first, second) + sum_series(n-2, first, second)



#test block to see if the functions are working properly
print('fibonacci(5) = 5 | Actual output is ', fibonacci(5))
print('fibonacci(10) = 55 | Actual output is ', fibonacci(10))
print('lucas(5) = 11 | Actual output is ', lucas(5))
print('lucas(10) = 123 | Actual output is ', lucas(10))
print('sum_series(5, 0, 1) = 5 | Actual output is ', sum_series(5, 0, 1))
print('sum_series(5) = 5 | Actual output is ', sum_series(5))
print('sum_series(10) = 55 | Actual output is ', sum_series(10))
print('sum_series(2, 10, 2) = 12 | Actual output is ', sum_series(2, 10, 2))
print('sum_series(3, 10, 2) = 14 | Actual output is ', sum_series(3, 10, 2))
