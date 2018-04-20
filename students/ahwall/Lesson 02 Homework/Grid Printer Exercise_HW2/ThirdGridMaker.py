
def print_grid(x, y):

    plus = "+"
    space = " "
    minus = "-"
    post = "|"

    def topmidbot(x, y):
        for i in range(x):
            print(plus + (space + minus) * y + space, end='')
        print(plus)

    def postsegment(x, y):
        if y % 2 == 0:
            z = y
        else:
            z = y
        w = 1 + (2 * z)
        for i in range(y):
            print(((post + (space * w)) * x), end='')
            print(post)

    def grid_units(x, y):
        for i in range(x):
            topmidbot(x, y)
            postsegment(x, y)
        topmidbot(x, y)

    grid_units(x, y)
