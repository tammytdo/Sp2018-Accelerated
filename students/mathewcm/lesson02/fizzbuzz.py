#Fizzbuzz exercise Lesson02 UW Python Accelerated

def fizzbuzz():
    """
    fizzbuzz() function prints a range of numbers from 1 to 100 with all values that are a factor of 3 replaced with the word Fizz and all the values that are a factor of 5 replaced with the word Buzz. Except those numbers that are a factor of both; they are replaced with the word Fizzbuzz.
    """
    for i in range(101):
        if i % 3 == 0 and i % 5 == 0:
            print("Fizzbuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizzbuzz()
