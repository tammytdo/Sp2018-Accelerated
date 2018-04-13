# Create a grid:
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
#
# + - + - +
# |   |   |
# + - + - +
# |   |   |
# + - + - +
#
# + - - - - - - - + - - - - - - - +
# |               |               |
# |               |               |
# |               |               |
# |               |               |
# |               |               |
# |               |               |
# |               |               |
# + - - - - - - - + - - - - - - - +
# |               |               |
# |               |               |
# |               |               |
# |               |               |
# |               |               |
# |               |               |
# |               |               |
# + - - - - - - - + - - - - - - - +


def print_test():
    p = '+'
    m = '-'
    s = ' '
    c = '|'
    side = p + s + 4 * (m + s)
    row = (2 * side) + p
    col = c + (len(side) - 1) * s
    column = (2 * col) + c
    print(row)
    for i in range(0, 4):
        print(column)
    print(row)
    for i in range(0, 4):
        print(column)
    print(row)
    return


print_test()
