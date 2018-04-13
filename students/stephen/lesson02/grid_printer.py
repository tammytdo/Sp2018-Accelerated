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

# Part 2
# Create a function print_grid() such that
# print_grid(3) would print a smaller grid:
# + - + - +
# |   |   |
# + - + - +
# |   |   |
# + - + - +
# print_grid(15) prints a larger grid:
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


def print_grid(n):
    p = '+'
    m = '-'
    s = ' '
    c = '|'
    side = p + s + (n // 2) * (m + s)
    row = (2 * side) + p
    col = c + (len(side) - 1) * s
    column = (2 * col) + c
    print(row)
    for i in range(0, n // 2):
        print(column)
    print(row)
    for i in range(0, n // 2):
        print(column)
    print(row)
    return


print_grid(3)

print_grid(15)
