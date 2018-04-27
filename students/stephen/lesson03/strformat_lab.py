#!/usr/bin/env python3

# Task One
# Write a format string that will take the following four element tuple:
# ( 2, 123.4567, 10000, 12345.67)
# and produce:
# 'file_002 :   123.46, 1.00e+04, 1.23e+04'

four = ( 2, 123.4567, 10000, 12345.67)

four_format = 'file_{:0>3d} : {:.2f}, {:.2e}, {:.2e}'.format(four[0], four[1], four[2], four[3])

print(four_format)

# Task Two
# Using your results from Task One, repeat the exercise, but this time using
# an alternate type of format string (hint: think about alternative ways to
# use .format() (keywords anyone?),
# and also consider f-strings if you’ve not used them already).

first = '{:0>3d}'.format(four[0])
second = '{:.2f}'.format(four[1])
third = '{:.2e}'.format(four[2])
fourth = '{:.2e}'.format(four[3])

four_format2 = f'file_{first} : {second}, {third}, {fourth}'

print(four_format2)

# Task Three
# Dynamically Building up Format Strings
# Rewrite:
# "the 3 numbers are: {:d}, {:d}, {:d}".format(1,2,3)
# to take an arbitrary number of values.

def formatter(in_tuple):
    seed = 'the {} numbers are: '.format(len(in_tuple)) + (len(in_tuple) * '{:d}, ')
    return seed[:-2].format(*in_tuple)

assert formatter((2,3,5)) == 'the 3 numbers are: 2, 3, 5'
assert formatter((2,3,5,7,9)) == 'the 5 numbers are: 2, 3, 5, 7, 9'

print('Task Three assertions have been passed.')

# Task Four
# Given a 5 element tuple:
# ( 4, 30, 2017, 2, 27)
# use string formating to print:
# '02 27 2017 04 30'

t4 = ( 4, 30, 2017, 2, 27)

new_string = '{:0>2d} {:d} {:d} {:0>2d} {:d}'.format(t4[3], t4[4], t4[2], t4[0], t4[1])
print(new_string)

# Task Five
# Here’s a task for you: Given the following four element list:
# ['oranges', 1.3, 'lemons', 1.1]
# Write an f-string that will display:
# The weight of an orange is 1.3 and the weight of a lemon is 1.1

elements = ['oranges', 1.3, 'lemons', 1.1]

formatted = f'The weight of an {elements[0][:-1]} is {elements[1]} and the weight of a {elements[2][:-1]} is {elements[3]}'

print(formatted)

# Now see if you can change the f-string so that it displays the names of the fruit
# in upper case, and the weight 20% higher (that is 1.2 times higher).

formatted2 = f'The weight of an {elements[0][0:1].upper() + elements[0][1:-1]} is {1.2 * elements[1]} and the weight of a {elements[2][0:1].upper() + elements[2][1:-1]} is {1.2 * elements[3]}'

print(formatted2)

# Task Six
# Write some Python code to print a table of several rows, each with a name, an age and
# a cost. Make sure some of the costs are in the hundreds and thousands to test your
# alignment specifiers. And for an extra task, given a tuple with 10 consecutive numbers,
# can you work how to quickly print the tuple in columns that are 5 charaters wide?
# It’s easily done on one short line!

row1 = '{:12} {:>3d} {:>10}'.format('John', 10, '$1400.56')
row2 = '{:12} {:>3d} {:>10}'.format('Elizabeth', 60, '$14.56')
row3 = '{:12} {:>3d} {:>10}'.format('Tom', 30, '$14000.56')

print(row1)
print(row2)
print(row3)

# And for an extra task, given a tuple with 10 consecutive numbers,
# can you work how to quickly print the tuple in columns that are 5 charaters wide?
# It’s easily done on one short line!

test = tuple(range(1,11))
print(('{:5d}' * len(test)).format(*test))