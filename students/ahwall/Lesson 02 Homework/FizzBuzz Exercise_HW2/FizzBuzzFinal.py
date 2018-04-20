'''
This function uses a for loop with if elif else conditions to list numbers
1 to 100.  If the number is divisible by 3, then Fizz is printed.  If divisible
by 5, then Buzz is printed.  If divisible by both, FizzBuzz is printed.  The
number is printed if none of the conditions are met.
'''


def FizzBuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
