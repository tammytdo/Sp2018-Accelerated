
'''
This program uses an outer function with 2 imbedded functions to create the
grid.  The x value is passed to the inner functions to determine the
specifications
'''


def print_grid(x):

    # defines variable used in the body of the functions
    plus = "+"
    space = " "
    minus = "-"
    post = "|"

    # function that creates the top of the box, use parameters to define
    # specifications
    def topmidbot(x):
        y = x // 2
        print(plus, end='')
        print((space + minus) * y, end='')
        print(space, end='')
        print(plus, end='')
        print((space + minus) * y, end='')
        print(space, end='')
        print(plus)


    # function that creates the walls of the box, use parameters to define
    # specifications
    def postsegment(x):
        if x % 2 == 0:
            z = x + 1
        else:
            z = x
        y = x // 2
        for i in range(y):
            print((post + (space * z) + post + (space * z) + post))

    # calls the functions
    topmidbot(x)
    postsegment(x)
    topmidbot(x)
    postsegment(x)
    topmidbot(x)
