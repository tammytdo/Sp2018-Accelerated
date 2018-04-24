'''
Jay Johnson Grid Printer

Write a function that draws a grid like the following:

+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +



'''
import math

# fuction to print grid
def print_grid_simple_function(n):
    print('+ ' + '- ' * n  + '+ ' + '- ' * n  + '+')
    print('|' + '  ' * n + ' |'  + '  ' * n + ' |')
    print('|' + '  ' * n + ' |'  + '  ' * n + ' |')
    print('|' + '  ' * n + ' |'  + '  ' * n + ' |')
    print('|' + '  ' * n + ' |'  + '  ' * n + ' |')
    print('+ ' + '- ' * n  + '+ ' + '- ' * n  + '+')
    print('|' + '  ' * n + ' |'  + '  ' * n + ' |')
    print('|' + '  ' * n + ' |'  + '  ' * n + ' |')
    print('|' + '  ' * n + ' |'  + '  ' * n + ' |')
    print('|' + '  ' * n + ' |'  + '  ' * n + ' |')
    print('+ ' + '- ' * n  + '+ ' + '- ' * n  + '+')

# calling the function to print the grid
print_grid_simple_function(4)

'''
One of the points of writing fuctions is so you can write code that does similar things,
but customized by the values of input parameters.
So what if we want to be able to print that grid at an arbitrary size?

Write a function print_grid(n) that takes one integer argument and prints a grid just like before
, BUT the size of the grid is given by the argument.

For example, print_grid(11) prints the grid in the above picture.

print_grid(3) would print a smaller grid:

+ - + - +
|   |   |
+ - + - +
|   |   |
+ - + - +
print_grid(15) prints a larger grid:

+ - - - - - - - + - - - - - - - +
|               |               |
|               |               |
|               |               |
|               |               |
|               |               |
|               |               |
|               |               |
+ - - - - - - - + - - - - - - - +
|               |               |
|               |               |
|               |               |
|               |               |
|               |               |
|               |               |
|               |               |
+ - - - - - - - + - - - - - - - +
This problem is underspecified. Do something reasonable.
'''

def print_grid(n):
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

print_grid(3)
print_grid(15)


'''
Write a function that draws a similar grid with a specified number of rows and columns, and with each cell a given size.

For example, print_grid2(3,4) results in:

+ - - - - + - - - - + - - - - +
|         |         |         |
|         |         |         |
|         |         |         |
|         |         |         |
+ - - - - + - - - - + - - - - +
|         |         |         |
|         |         |         |
|         |         |         |
|         |         |         |
+ - - - - + - - - - + - - - - +
|         |         |         |
|         |         |         |
|         |         |         |
|         |         |         |
+ - - - - + - - - - + - - - - +
(three rows, three columns, and each grid cell four “units” in size)

What to do about rounding? – you decide.

Another example: print_grid2(5,3):
+ - - - + - - - + - - - + - - - + - - - +
|       |       |       |       |       |
|       |       |       |       |       |
|       |       |       |       |       |
+ - - - + - - - + - - - + - - - + - - - +
|       |       |       |       |       |
|       |       |       |       |       |
|       |       |       |       |       |
+ - - - + - - - + - - - + - - - + - - - +
|       |       |       |       |       |
|       |       |       |       |       |
|       |       |       |       |       |
+ - - - + - - - + - - - + - - - + - - - +
|       |       |       |       |       |
|       |       |       |       |       |
|       |       |       |       |       |
+ - - - + - - - + - - - + - - - + - - - +
|       |       |       |       |       |
|       |       |       |       |       |
|       |       |       |       |       |
+ - - - + - - - + - - - + - - - + - - - +
'''

def print_grid2(c,n):
    print('+' + " - "*n + '+')
    for i in range( n ):
        print('|' + "   "*n + '|')
    print('+' + " - "*n + '+')
    #could not get multiple boxes working

print_grid2(0,3)
