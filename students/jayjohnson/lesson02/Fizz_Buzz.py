'''
Jay Johnson Fizz Buzz

x Write a program that prints the numbers from 1 to 100 inclusive.
x But for multiples of three print “Fizz” instead of the number.
x For the multiples of five print “Buzz” instead of the number.
x For numbers which are multiples of both three and five print “FizzBuzz” instead.
'''
# loop logic
guess = False

# count set to 100
test_num = 100

# loop
while guess == False:
    if (test_num % 3 == 0) and (test_num % 5 == 0):
        print("FizzBuzz")
    elif (test_num % 3 == 0):
        print("Fizz")
    elif (test_num % 5 == 0):
        print("Buzz")
    else:
        print(test_num)

    test_num = test_num - 1
    if test_num == 0:
        break
