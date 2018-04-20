'''
Jay Johnson lesson 02 notes

'''

# functions make programs
def addOne(x):
    result = x + 1
    return result

# key word arguments or qwards
# positional arguments
# you can leave off the return statement
# you can return multiple values
#def add():
#   return 1, 2, "blah"
# will return it as a tuple
# local variable = variables in scope
# pep8???

# if __name__=="__main__":
# a python file can be used as a script or imported as a module

#github
# main commands
# 1) git add
# 2) git commit
# 3) git push
# 4) git pull upstream master

'''
import math

def fibonacci(n):
    for i in range(n)
        numb = (n-2) + (n-1)
        print(numb)

fibonacci(4)

'''
'''
import os

# Program to display the Fibonacci sequence up to n-th term where n is provided by the user
def fibonacci(n):
    # first two terms
    n1 = 0
    n2 = 1
    count = 0
# check if the number of terms is valid
    if n <= 0:
        print("Please enter a positive integer")
    elif n == 1:
        print("Fibonacci sequence upto",n,":")
        print(n1)
    else:
        print("Fibonacci sequence up to",n,":")
        while count < n:
            print(n1,end=' , ')
            nth = n1 + n2
       # update values
            n1 = n2
            n2 = nth
            count += 1

    os.system('cls')
    print(n1)

fibonacci(10)
'''


'''
def print_grid2(c,n):
    grid_count_upper = math.floor(n/2)
    grid_count_lower = math.floor(n/2)
    print('+ ' + '- '*math.floor(n/2) + '+ ' + '- '*math.floor(n/2) + '+'  )
    for i in range( grid_count_upper ):
        print('| ' + '  '*math.floor(n/2) + '| ' + '  '*math.floor(n/2) + '|'  )
    print('+ ' + '- '*math.floor(n/2) + '+ ' + '- '*math.floor(n/2) + '+'  )
    for i in range( grid_count_lower):
        print('| ' + '  '*math.floor(n/2) + '| ' + '  '*math.floor(n/2) + '|'  )
        grid_count_lower = grid_count_lower - 1
    print('+ ' + '- '*math.floor(n/2) + '+ ' + '- '*math.floor(n/2) + '+'  )
'''

'''
def print_grid2(c,n):
    print('+' + " - "*n + '+')
    for i in range( n ):
        print('|' + "   "*n + '|')
    print('+' + " - "*n + '+')

print_grid2(0,5)
'''
