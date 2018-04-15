#!/usr/bin/env python

"""Print grids based on increasingly complex and scalable required parameters"""
def grid_printer_1():
    print("+", "- " * 4, "+", "- " * 4, "+")
    print("|", " " * 8, "|", " " * 8, "|")
    print("|", " " * 8, "|", " " * 8, "|")
    print("|", " " * 8, "|", " " * 8, "|")
    print("|", " " * 8, "|", " " * 8, "|")
    print("+", "- " * 4, "+", "- " * 4, "+")
    print("|", " " * 8, "|", " " * 8, "|")
    print("|", " " * 8, "|", " " * 8, "|")
    print("|", " " * 8, "|", " " * 8, "|")
    print("|", " " * 8, "|", " " * 8, "|")
    print("+", "- " * 4, "+", "- " * 4, "+")


def grid_printer_2(unit_size):
    side_len = unit_size // 2
    print("+", "- " * side_len, "+", "- " * side_len, "+")

    for row in range(side_len):
        print("|", " " * (unit_size - 1), "|", " " * (unit_size - 1), "|")

    print("+", "- " * side_len, "+", "- " * side_len, "+")

    for row in range(side_len):
        print("|", " " * (unit_size - 1), "|", " " * (unit_size - 1), "|")

    print("+", "- " * side_len, "+", "- " * side_len, "+")

def grid_printer_3(num_units, unit_size):
    pass


if __name__ == "__main__":

# grid_printer_1()
# grid_printer_2(15)
