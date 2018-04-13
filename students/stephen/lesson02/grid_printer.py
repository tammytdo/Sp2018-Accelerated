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

# Write a function that draws a similar grid with a specified number of
# rows and columns, and with each cell a given size.

# For example, print_grid2(3,4) results in:

# + - - - - + - - - - + - - - - +
# |         |         |         |
# |         |         |         |
# |         |         |         |
# |         |         |         |
# + - - - - + - - - - + - - - - +
# |         |         |         |
# |         |         |         |
# |         |         |         |
# |         |         |         |
# + - - - - + - - - - + - - - - +
# |         |         |         |
# |         |         |         |
# |         |         |         |
# |         |         |         |
# + - - - - + - - - - + - - - - +
# (three rows, three columns, and each grid cell four “units” in size)


def print_grid2(x, y):
    p = '+'
    m = '-'
    s = ' '
    c = '|'
    side = p + s + y * (m + s)
    row = (x * side) + p
    col = c + (len(side) - 1) * s
    column = (2 * col) + c
    for i in range(0, x):
        print(row)
        for j in range(0, y):
            print(column)
    print(row)
    return


print_grid2(3, 4)
