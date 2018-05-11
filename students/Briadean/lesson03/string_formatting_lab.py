# !/usr/bin/env python3

# Task 1
"""Takes (2, 123.4567, 10000, 12345.67) and produces file_002 :   123.46, 1.00e+04, 1.23e+04"""

print("\nfile_{:03d} : {:10.2f}, {:.2e}, {:.2e}".format(2, 123.4567, 10000, 12345.67))

# Task 2
"""Refactor task 1 to utilize f strings."""

tupe = (2, 123.4567, 10000, 12345.67)
print(f"file_{tupe[0]:03d} : {tupe[1]:10.2f}, {tupe[2]:.2e}, {tupe[3]:.2e}")

# Task 3
""" Refactor 'the 3 numbers are: {:d}, {:d}, {:d}".format(1,2,3)' to accept an arbitrary number of values."""


def formatter(tupe):
    form_str = "The {} numbers are: ".format(len(tupe))
    form_str += ", ".join(["{}"] * len(tupe))
    return form_str.format(* tupe)

print()
print(formatter((2, 123.4567, 10000, 12345.67)))
print(formatter((1, 3, 5, 7, 9, 11)))

# Task 4
"""Use string formatting to print 02 27 2017 04 30 from ( 4, 30, 2017, 2, 27)."""

print("\n{3:02d} {4:02d} {2} {0:02d} {1:02d}".format(4, 30, 2017, 2, 27))

# Task 5
"""Using['oranges', 1.3, 'lemons', 1.1] write an f-string that will display:
'The weight of an orange is 1.3 and the weight of a lemon is 1.1
Then change the f-string so that it displays the names of the fruit in upper case, and the weight 20% higher."""

lst = ['oranges', 1.3, 'lemons', 1.1]
print(f"\nThe weight of an {lst[0]} is {lst[1]} and the weight of a {lst[2]} in {lst[3]}")
print(f"The weight of an {lst[0].upper()} is {lst[1] * 1.2} and the weight of a {lst[2].upper()} in {lst[3] * 1.2}")

# Task 6
"""
Print a table of several rows, each with a name, an age and a cost. 

And for an extra task, given a tuple with 10 consecutive numbers, can you work how to quickly print 
the tuple in columns that are 5 charaters wide? It’s easily done on one short line!
"""
dict = {"Michael": [20, 10000],
        "Leah": [18, 1500],
        "Noah": [16, 4500],
        "Chloe": [14, 3250]}

table_line = []
for (name, info) in dict.items():
    name = name
    age = info[0]
    cost = info[1]
    table_line.append((name, age, cost))


header = "\n{:20} | {:15} | {:15}".format("Name", "Age", "Cost")

table = []
table.append(header)
table.append("-" * 53)
[table.append("{:20} {:15} {:15,.2f}".format(* line)) for line in table_line]
display_table = "\n".join(table)

print(display_table)

# Bonus

tupe =(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print()
print(("{:<5}" * len(tupe)).format(* tupe))
