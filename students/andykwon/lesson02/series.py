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
    '''takes in 3 parameters. num1 is the input value. option1 and option 2 are optional values. 
    If those values equal 2 and 1 respectively, then the Lucas number is found usiung the inputted value.
    Otherwise, the function will return the Fibonacci number of the input. 
    Note that the function is defaulted to return the Fibonacci number. 
    '''

    # Lucas number function
    def luc(n):

        if n == 0: 
            return 2
        elif n == 1: 
            return 1
        else: 
            return luc(n-1) + luc(n-2)

    # Fibonacci number function
    def fib(n):

        if n == 0: 
            return 0
        elif n == 1: 
            return 1
        else: 
            return fib(n-1) + fib(n-2)

    # if the optional parameters are 2 and 1, then the returns the Lucas formula. Otherwise, it will return the Fibonacci number. 
    if option1 == 2 and option2 == 1:
        return luc(num1)

    else:
        return fib(num1)


print(sum_series(7, 2, 4))
print(lucas(7))
print(fibonacci(7))

#Tests:

import unittest

class TestSeriesNumbers(unittest.TestCase):

    def test_lucas(self):
        '''
        Testing the Lucas number to ensure proper output: 10th lucas number is 123
        '''
        self.assertEqual(lucas(10), 123)

    def test_fibonacci(self):
        '''
        Testing the Fibonacci number to ensure proper output: 10th Fibonacci number is 55
        '''
        self.assertEqual(fibonacci(10), 55)

    def test_sum_series_lucas(self):
        '''
        Testing that the sum_series function, with proper optional parameters, outputs the proper Lucas Number
        '''
        self.assertEqual(sum_series(10, 2, 1), 123)

    def test_sum_series_fib1(self):
        '''
        Testing that the sum_series function defaults to the Fibonacci number when no optional parameters are given
        '''
        self.assertEqual(sum_series(10), 55)

    def test_sum_series_fib2(self):
        '''
        Testing that the sum_series function defaults to the Fibonacci number when 1 optional parameter is given
        '''
        self.assertEqual(sum_series(10, 1), 55)

    def test_sum_series_fib3(self):
        '''        
        Testing that the sum_series function defaults to the Fibonacci number when optional parameters are not 2 and 1
        '''
        self.assertEqual(sum_series(10, 55, 100), 55)

if __name__ == '__main__':
    unittest.main()



