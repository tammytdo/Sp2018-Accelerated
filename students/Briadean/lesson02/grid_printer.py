#!/usr/bin/env python

"""Print an exact replica of the example grid"""
def grid_printer_1():
    row = "+" + " - " * 4 + "+" + " - " * 4 + "+"
    column = "|" + " " * 12 + "|" + " " * 12 + "|"

    print(row)
    for x in range(4):
        print(column)
    print(row)
    for x in range(4):
        print(column)
    print(row)

"""Print a grid whose unit size is determined by user input"""
def grid_printer_2(unit_size):
    side_len = unit_size // 2
    row = "+" + " - " * side_len + "+" + " - " * side_len + "+"
    column = "|" + " " * (side_len * 3) + "|" + " " * (side_len * 3) + "|"

    print(row)
    for x in range(side_len):
        print(column)
    print(row)
    for x in range(side_len):
        print(column)
    print(row)

"""Print a grid whose unit size and number of contained units are determined by user input"""
def grid_printer_3(unit_size, num_units):
    side_len = unit_size // 2
    row = (("+" + " - " * side_len) * num_units + "+\n")
    column = (("|" + (" " * side_len * 3)) * num_units + "|\n")
    column_block = column * side_len
    box = column_block.join([row] * (num_units + 1))
    print(box)


# grid_printer_1()
# grid_printer_2(7)
# grid_printer_3(4, 5)
