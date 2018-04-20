'''
This program uses an outer function with 2 imbedded functions to create the
grid.  The x and y values are passed to the inner functions to determine the
specifications
'''


def print_grid(x, y):
    # defines variable used in the body of the functions
    plus = "+"
    space = " "
    minus = "-"
    post = "|"

# function that creates the top of the box, use parameters to define
# specifications

    def topmidbot(x, y):
        for i in range(x):
            print(plus + (space + minus) * y + space, end='')
        print(plus)

# function that creates the walls of the box, use parameters to define
# specifications

    def postsegment(x, y):
        if y % 2 == 0:
            z = y
        else:
            z = y
        w = 1 + (2 * z)
        for i in range(y):
            print(((post + (space * w)) * x), end='')
            print(post)

# This function uses a loop to create a grid that has the same number of
# box in the x direction as the y direction

    def grid_units(x, y):
        for i in range(x):
            topmidbot(x, y)
            postsegment(x, y)
        topmidbot(x, y)

# calls the function that creates the full grid
    grid_units(x, y)
