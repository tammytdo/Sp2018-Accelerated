#=========================================================================================
#Name: FizzBuzz
#Author: Wesley Wang
#Date: 4/12/2018
#=========================================================================================

def fizz_buzz():
    result = ""
    for i in range(1, 101):
        #Return
        if i%3 != 0 and i%5 !=0:
            result += str(i)
        if i%3 == 0:
            result += "Fizz"
        if i%5 == 0:
            result += "Buzz"
        result += '\n'
    return result

print(fizz_buzz())