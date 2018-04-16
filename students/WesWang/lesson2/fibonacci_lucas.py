#=========================================================================================
#Name: Fibonacci Series & Lucas Number
#Author: Wesley Wang
#Date: 4/12/2018
#=========================================================================================

def sum_series(n0, n1, nth):
    prev = n0
    current = n1
    if nth > 2:
        for i in range(nth-2):
            prev, current = current, prev + current
    if nth == 1:
        return prev
    elif nth <= 0:
        return "Please enter a non-zero, positive number!"
    else:
        return current

def fibonacci(nth):
    return sum_series(0, 1, nth)

def lucas(nth):
    return sum_series(2, 1, nth)


print(fibonacci(5))
print(lucas(5))

