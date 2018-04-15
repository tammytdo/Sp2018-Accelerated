'''
Part 1: Write a function that draws a grid like the following:
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
a = '+ '
b = '- ' * 4
c = '| '
d = '  ' * 4
x = str('{}{}{}{}{}\n').format(a, b, a, b, a)
y = str('{}{}{}{}{}\n').format(c, d, c, d, c)
print('Part 1: Write a function that draws a grid\n'+x+y*4+x+y*4+x)
'''
Part 2: Make it a function
Write a function print_grid(n) that takes one integer argument and prints a grid just like before, BUT the size of the grid is given by the argument.
'''
def print_grid(x):
    n = x // 2
    a = '+ '
    b = '- ' * n
    c = '| '
    d = '  ' * n
    x = str('{}{}{}{}{}\n').format(a, b, a, b, a)
    y = str('{}{}{}{}{}\n').format(c, d, c, d, c)
    print('Part 2: Write a function print_grid(n) that takes one integer argument and prints a grid just like before, BUT the size of the grid is given by the argument.\n'+x+y*n+x+y*n+x)

print_grid(15)
'''
Part 3: Write a function that draws a similar grid with a specified number of rows and columns, and with each cell a given size.

Note = Exercise is to print length * width based on first input and number of lines within each square by second input
'''
def print_grid2(rows_columns=1,size=1):
    #Horizontal Components
    a = '+ '
    b = '- ' * size
    c = '| '
    d = '  ' * size
    x = str('{}{}\n').format((a+b)*rows_columns,a)
    y = str('{}{}\n').format((c+d)*rows_columns,c)
    #Vertical Components
    single_row = x+y*size
    #Grid
    grid = single_row*rows_columns+x
    print(grid)

print('Part 3: Write a function that draws a similar grid with a specified number of rows and columns, and with each cell a given size.\n')
print_grid2(3,4)
print_grid2(5,3)
