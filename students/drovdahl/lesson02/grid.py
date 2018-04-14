#! /usr/local/bin/python3


def grid():
    '''
    This function will draw a static grid with 4 quadrants that are 6x6.
    A '+' will be used in the corners
    A '-' or '|' will be used in between the corners
    '''
    print(2*('+' + 4*('-')) + '+')
    print((2*('|' + 4*(' ')) + '|'))
    print((2*('|' + 4*(' ')) + '|'))
    print((2*('|' + 4*(' ')) + '|'))
    print((2*('|' + 4*(' ')) + '|'))
    print(2*('+' + 4*('-')) + '+')
    print((2*('|' + 4*(' ')) + '|'))
    print((2*('|' + 4*(' ')) + '|'))
    print((2*('|' + 4*(' ')) + '|'))
    print((2*('|' + 4*(' ')) + '|'))
    print(2*('+' + 4*('-')) + '+')


def print_grid(n):
    '''
    This function will print a grid with four quadrants of an arbritrary size.
    The argument will define the numbers of rows/columns in the grid.
    If the argument needs to be adjusted to provide equal sized quadrants, it
    will be increased by a value of 1.
    '''
    # Adjust the argument if necessary to ensure all four quadrants will have
    # equal sizes.
    if n % 2 == 1:
        pass
    else:
        n = n + 1
    # define the number of '-' or '|' characters between the corners ('+')
    x = int((n-1)/2) - 1
    # top row
    print('+' + x*'-' + '+' + x*'-' + '+')
    for i in range(x):
        print('|' + x*' ' + '|' + x*' ' + '|')
    print('+' + x*'-' + '+' + x*'-' + '+')
    for i in range(x):
        print('|' + x*' ' + '|' + x*' ' + '|')
    print('+' + x*'-' + '+' + x*'-' + '+')


grid()
print_grid(11)
