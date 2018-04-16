def fibonacci(n):
    '''
    #The Fibonacci number requires values for the 0th and 1st values as the sequence cannot be 
    completed. Goes into an infinite loop i think...
    '''
    if n == 0: 
        return 0
    elif n == 1: 
        return 1
    else: 
        return fibonacci(n-1) + fibonacci(n-2)





def lucas(n):

    '''
    The Lucas number requires values for the 0th and 1st values. Different values than from 
    Fibonnaci for the first two values. 
    '''

    if n == 0: 
        return 2
    elif n == 1: 
        return 1
    else: 
        return lucas(n-1) + lucas(n-2)




def sum_series(num1, option1 = 0, option2 = 0):

    def luc(n):

        if n == 0: 
            return 2
        elif n == 1: 
            return 1
        else: 
            return luc(n-1) + luc(n-2)

    def fib(n):

        if n == 0: 
            return 0
        elif n == 1: 
            return 1
        else: 
            return fib(n-1) + fib(n-2)


    if option1 == 2 and option2 == 1:
        return luc(num1)

    else:
        return fib(num1)


print(sum_series(7, 2, 4))
print(lucas(7))
print(fibonacci(7))

