#! /usr/local/bin/python3


'''
Write some functions that take a sequence as an argument and return a copy of
that sequence with modifications:

 with the first and last items exchanged.
 with every other item removed.
 with the first and last 4 items removed, and every other item in between.
 with the elements reversed (just with slicing).
 with the last third, then first third, then the middle third in the new order.
'''

a_string = 'this is a string'
a_tuple = (2, 54, 13, 12, 5, 32)
a_list = [1, 2, 3, 4, 5, 6, 7]


def first_last_flip(seq):
    '''
    This function exchanges the first and last elements of the sequence arg
    It works with tuples, lists, and string sequences
    '''
    # process for tuples
    while type(seq) is tuple:
        new_seq = list(seq)
        new_seq2 = new_seq[1:-1]
        new_seq2.insert(0, seq[-1])
        new_seq2.append(seq[0])
        return tuple(new_seq2)
    # process for lists
    while type(seq) is list:
        new_seq = seq[1:-1].copy()
        new_seq.insert(0, seq[-1])
        new_seq.append(seq[0])
        return new_seq
    # process for string sequences
    new_seq = seq[-1] + seq[1:-1] + seq[1]
    return new_seq


print(first_last_flip(a_string))
print(first_last_flip(a_tuple))
print(first_last_flip(a_list))
