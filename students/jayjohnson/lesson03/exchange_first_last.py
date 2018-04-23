'''
Jay Johnson
exchange first last
/////
Goal
Get the basics of sequence slicing down.

Tasks
Write some functions that take a sequence as an argument, and return a copy of that sequence:

x with the first and last items exchanged.
x with every other item removed.
X with the first and last 4 items removed, and every other item in between.
x with the elements reversed (just with slicing).
x with the last third, then first third, then the middle third in the new order.
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

# the first and last items exchanged.
def exchange_first_last(seq):

    temp = seq
    temp[1:-1]
    a_new_sequence = temp[-1:] + temp[1:-1] + temp[:1]

    return a_new_sequence

# with the elements reversed (just with slicing).
def elements_reversed(seq):

    a_new_sequence = tuple(seq)

    return a_new_sequence[::-1]

# with every other item removed.
def every_other(seq):

    a_new_sequence = tuple(seq)

    a_newer_sequence = []
    #gives every other value
    a_newer_sequence = a_new_sequence[0:int(len(a_new_sequence)):2]

    return a_newer_sequence

# with the first and last 4 items removed, and every other item in between.
def first_last_four(seq):

    a_new_sequence = tuple(seq)

    return a_new_sequence[4:-4]

#with the last third, then first third, then the middle third in the new order.

def last_first_middle(seq):

    last = []
    first = []
    middle = []

    a_new_sequence = tuple(seq)
    seq_len = len(a_new_sequence)
    last = a_new_sequence[int(seq_len / 2):]
    first = a_new_sequence[:-int(seq_len / 2)]
    middle = a_new_sequence[2:-2]

    return last + first + middle

print(elements_reversed(a_string))
print(elements_reversed(a_tuple))
print(exchange_first_last(a_string))
print(exchange_first_last(a_tuple))
print(every_other(a_string))
print(every_other(a_tuple))
print(first_last_four(a_string))
print(first_last_four(a_tuple))
print(last_first_middle(a_string))
print(last_first_middle(a_tuple))
