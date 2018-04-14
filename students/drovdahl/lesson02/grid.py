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
    This function will print a grid of an arbritrary size using the argument to
    define the size of the quadrants.
    '''


grid()
