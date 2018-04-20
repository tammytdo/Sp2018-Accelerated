
def print_grid(x):

    plus = "+"
    space = " "
    minus = "-"
    post = "|"

    def topmidbot(x):
        y = x // 2
        print(plus, end='')
        print((space + minus) * y, end='')
        print(space, end='')
        print(plus, end='')
        print((space + minus) * y, end='')
        print(space, end='')
        print(plus)


# add in if statment for even vs odd entry values.
    def postsegment(x):
        if x % 2 == 0:
            z = x + 1
        else:
            z = x
        y = x // 2
        for i in range(y):
            print((post + (space * z) + post + (space * z) + post))

    topmidbot(x)
    postsegment(x)
    topmidbot(x)
    postsegment(x)
    topmidbot(x)
