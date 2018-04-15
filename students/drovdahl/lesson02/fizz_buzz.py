#! /usr/local/bin/python3
'''
This program prints numbers 1-100
For numbers that are multiples of 3, print 'Fizz' instead
For numbers that are multiples of 5, print 'Buzz' instead
For numbers that are multiples of both 3 and 5, print 'FizzBuzz' instead
'''

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    if i % 3 == 0:
        print('Fizz')
    if i % 5 == 0:
        print('Buzz')
    print(i)
