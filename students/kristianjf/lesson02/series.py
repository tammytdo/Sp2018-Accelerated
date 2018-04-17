def Fibonacci(n):
    '''
    Step 1
    Create a new module series.py in the lesson02 folder in your student folder.
    In it, add a function called fibonacci.
    The function should have one parameter, n.
    The function should return the nth value in the fibonacci series.
    Ensure that your function has a well-formed docstring
    '''
    n = abs(n)
    n1 = 0
    n2 = 1
    fib_list = [n1, n2]
    for x in range(1,n):
        n3 = n1 + n2
        fib_list.append(n3)
        n1 = fib_list[-2]
        n2 = fib_list[-1]
    return fib_list, fib_list[n]

print('Fibonacci List: {} \nFibonacci Value: {}'.format(Fibonacci(7)[0],Fibonacci(7)[1]))

def Lucas(n):
    '''
    The Lucas Numbers (Links to an external site.)Links to an external site. are a related series of integers that start with the values 2 and 1
    '''
    n = abs(n)
    n1 = 2
    n2 = 1
    luc_list = [n1, n2]
    for x in range(1,n):
        n3 = n1 + n2
        luc_list.append(n3)
        n1 = luc_list[-2]
        n2 = luc_list[-1]
    return luc_list, luc_list[n]

print('Lucas List: {} \nLucas Value: {}'.format(Lucas(7)[0],Lucas(7)[1]))

def sum_series(n, n1=0, n2=1):
    '''
    Add a third function called sum_series with one required parameter and two optional parameters. The required parameter will determine which element in the series to print. The two optional parameters will have default values of 0 and 1 and will determine the first two values for the series to be produced.

    Calling this function with no optional parameters will produce numbers from the fibonacci series. Calling it with the optional arguments 2 and 1 will produce values from the lucas numbers. Other values for the optional parameters will produce other series.
    '''
    n = abs(n)
    sum_list = [n1, n2]
    for x in range(1,n):
        n3 = n1 + n2
        sum_list.append(n3)
        n1 = sum_list[-2]
        n2 = sum_list[-1]
    return sum_list, sum_list[n]

print('Lucas List: {} \nLucas Value: {}'.format(Lucas(7)[0],Lucas(7)[1]))

'''
Assert Fibonacci function is equivalent to running sum_series function without optional arguments
'''
assert(Fibonacci(7) == sum_series(7))
'''
Assert Lucas function is equivalent to running sum_series function with optional arguments n1=0,n2=1
'''
assert(Lucas(7) == sum_series(7,n1=2,n2=1))
