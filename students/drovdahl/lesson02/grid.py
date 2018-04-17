#! /usr/local/bin/python3


def grid():
    '''
    This function will draw a static grid with 4 quadrants that are 6x6.
    A '+' character will be used in the corners
    A '-' or '|' character will be used in between the corners
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
    A '+' character will be used in the corners
    A '-' or '|' character will be used in between the corners
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
    # 1st and 2nd quadrant rows
    for i in range(x):
        print('|' + x*' ' + '|' + x*' ' + '|')
    # middle row
    print('+' + x*'-' + '+' + x*'-' + '+')
    # 3rd and 4th quadrant rows
    for i in range(x):
        print('|' + x*' ' + '|' + x*' ' + '|')
    # last row
    print('+' + x*'-' + '+' + x*'-' + '+')


def print_grid2(x, y):
    '''
    This function will print a grid with an arbritrary number of cells of
    an arbritrary size.
    The 'x' argument will define the number of cells in a given row or column.
    The 'y' argument will define the size of each cell.
    The grid will represent a perfect square with an equal number of horizontal
    and vertical characters.
    A '+' character will be used in the cell corners
    A '-' or '|' character will be used in between the cell corners
    '''
    # top row
    print(x*('+' + (y*'-')) + '+')
    # remaining rows
    for c in range(x):
        for i in range(y):
            print(x*('|' + (y*' ')) + '|')
        print(x*('+' + (y*'-')) + '+')


grid()
print_grid(11)
print_grid2(5, 3)
