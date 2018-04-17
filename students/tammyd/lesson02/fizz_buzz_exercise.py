"""The Classic Fizz Buzz Problem"""

"""This program prints the numbers from 1 to 100. For the multiples of three it prints “Fizz” instead of the number. For the multiples of five it  prints “Buzz” instead of the number.
For numbers which are multiples of both three and five it prints “FizzBuzz” instead."""


for i in range(1,101):
#multiples of 3
    if i % 3 == 0:
        print("Fizz")

#multiples of 5
    elif i % 5 == 0:
        print("Buzz")

#multiples of 3 as well as 5
    elif i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")

#not multiples of 3 or 5
    else:
        print(i)


