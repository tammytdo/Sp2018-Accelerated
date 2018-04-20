'''
Jay Johnson
exchange first last
/////
Goal
Get the basics of sequence slicing down.

Tasks
Write some functions that take a sequence as an argument, and return a copy of that sequence:

x with the first and last items exchanged.
with every other item removed.
with the first and last 4 items removed, and every other item in between.
x with the elements reversed (just with slicing).
with the last third, then first third, then the middle third in the new order.
NOTE: These should work with ANY sequence – but you can use strings to test, if you like.

Your functions should look like:

def exchange_first_last(seq):
    return a_new_sequence
Tests:
a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)

assert exchange_first_last(a_string) == "ghis is a strint"
assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)
Write a test or two like that for each of the above functions.
//////
'''
a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)

def exchange_first_last(seq):

    temp = seq
    temp[1:-1]
    a_new_sequence = temp[-1:] + temp[1:-1] + temp[:1]

    return a_new_sequence


def elements_reversed(seq):

    a_new_sequence = tuple(seq)

    return a_new_sequence[::-1]

print(elements_reversed(a_string))
print(elements_reversed(a_tuple))
print(exchange_first_last(a_string))
print(exchange_first_last(a_tuple))
