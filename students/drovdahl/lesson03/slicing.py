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

a_string = 'this is a really really long string'
a_tuple = (2, 54, 13, 12, 5, 32, 18, 6, 9, 1, 88, 60)
a_list = [2, 54, 13, 12, 5, 32, 18, 6, 9, 1, 88, 60]


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


def remove_every_other(seq):
    '''
    This function removes every other element in the sequence
    It works with tuples, lists, and string sequences
    '''
    # process for tuples
    while type(seq) is tuple:
        new_seq = list(seq)
        new_seq2 = new_seq[::2]
        return tuple(new_seq2)
    # process for lists
    while type(seq) is list:
        new_seq = seq[::2].copy()
        return new_seq
    # process for string sequences
    new_seq = seq[::2]
    return new_seq


def between_the_4s(seq):
    '''
    This function removes the first and last 4 items as well as every other
    item in between
    It works with tuples, lists, and string sequences
    '''
    # process for tuples
    while type(seq) is tuple:
        new_seq = list(seq)
        new_seq2 = new_seq[4:-4:2]
        return tuple(new_seq2)
    # process for lists
    while type(seq) is list:
        new_seq = seq[4:-4:2].copy()
        return new_seq
    # process for string sequences
    new_seq = seq[4:-4:2]
    return new_seq


def reverse(seq):
    '''
    This function reverses the sequence using just slicing methods
    It works with tuples, lists, and string sequences
    '''
    # process for tuples
    while type(seq) is tuple:
        new_seq = list(seq)
        new_seq2 = new_seq[::-1]
        return tuple(new_seq2)
    # process for lists
    while type(seq) is list:
        new_seq = seq[::-1].copy()
        return new_seq
    # process for string sequences
    new_seq = seq[::-1]
    return new_seq


def thirds_shuffle(seq):
    '''
    This function rearranges the last third, then the first third, then the
    middle third.
    It works with tuples, lists, and string sequences
    '''
    # determine length of each 'third' of the seq
    length = (len(seq)) // 3
    remainder = (len(seq)) % 3
    if remainder == 0:
        l1 = l2 = l3 = length
    if remainder == 1:
        l1 = length + 1
        l2 = l3 = length
    if remainder == 2:
        l1 = l2 = length + 1
        l3 = length
    # process for tuples
    while type(seq) is tuple:
        new_seq = list(seq)
        new_seq2 = new_seq[-l3:] + new_seq[:l1] + new_seq[l1:(l1 + l2)]
        return tuple(new_seq2)
    # process for lists
    while type(seq) is list:
        new_seq = seq[-l3:] + seq[:l1] + seq[l1:(l1 + l2)].copy()
        return new_seq
    # process for string sequences
    new_seq = seq[-l3:] + seq[:l1] + seq[l1:(l1 + l2)]
    return new_seq


assert(first_last_flip(a_tuple)) == (60, 54, 13, 12, 5, 32, 18, 6, 9, 1, 88, 2)
assert(first_last_flip(a_list)) == [60, 54, 13, 12, 5, 32, 18, 6, 9, 1, 88, 2]
assert(first_last_flip(a_string)) == 'ghis is a really really long strinh'
assert(remove_every_other(a_tuple)) == (2, 13, 5, 18, 9, 88)
assert(remove_every_other(a_list)) == [2, 13, 5, 18, 9, 88]
assert(remove_every_other(a_string)) == 'ti saral elyln tig'
assert(between_the_4s(a_tuple)) == (5, 18)
assert(between_the_4s(a_list)) == [5, 18]
assert(between_the_4s(a_string)) == ' saral elyln t'
assert(reverse(a_tuple)) == (60, 88, 1, 9, 6, 18, 32, 5, 12, 13, 54, 2)
assert(reverse(a_list)) == [60, 88, 1, 9, 6, 18, 32, 5, 12, 13, 54, 2]
assert(reverse(a_string)) == 'gnirts gnol yllaer yllaer a si siht'
assert(thirds_shuffle(a_tuple)) == (9, 1, 88, 60, 2, 54, 13, 12, 5, 32, 18, 6)
assert(thirds_shuffle(a_list)) == [9, 1, 88, 60, 2, 54, 13, 12, 5, 32, 18, 6]
assert(thirds_shuffle(a_string)) == 'long stringthis is a really really '

# assert(thirds_shuffle(a_string)) == 'long stringthis is a really really'
