# Write some functions that take a sequence as an argument,
# and return a copy of that sequence:
# with the first and last items exchanged.
# with every other item removed.
# with the first and last 4 items removed, and every other item in between.
# with the elements reversed (just with slicing).
# with the middle third, then last third, then the first third in the new order.

this = 'Test string'

that = list(range(1, 9))

def copy_seq(seq):
    """
    Return a copy of the original sequence.
    """
    return seq[:]

assert copy_seq(this) == this
assert copy_seq(that) == that

def first_last(seq):
    """
    Return the sequence wiwth the first and lat items exchanged.
    """
    return  seq[-1:len(seq)] + seq[1:-1] + seq[0:1]

assert first_last(this) == 'gest strinT'
assert first_last(that) == [8, 2, 3, 4, 5, 6, 7, 1]

def everyother(seq):
    """
    Return the sequence with with every other item removed.
    """
    return seq[::2]

assert everyother(this) == 'Ts tig'
assert everyother(that) == [1, 3, 5, 7]

def first_last4(seq):
    """
    Return the sequence with the first and last 4 items removed, and every other item in between
    """
    return seq[1:-4:2]

assert first_last4(this) == 'ets'
assert first_last4(that) == [2, 4]

def reverse(seq):
    """
    Return the sequence with the elements reversed (just with slicing).
    """
    return seq[::-1]

assert reverse(this) == 'gnirts tseT'
assert reverse(that) == [8, 7, 6, 5, 4, 3, 2, 1]

def thirds(seq):
    """
    Return the sequence with the middle third, then last third, then the first third in the new order.
    """
    first = len(seq) // 3
    second = first * 2
    return seq[first:second] + seq[second:] + seq[:first]

thirds_str = '1stthird2ndthird3rdthird'
thirds_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

assert thirds(thirds_str) == '2ndthird3rdthird1stthird'
assert thirds(thirds_list) == [4, 5, 6, 7, 8, 9, 1, 2, 3]

print('Assertions were successful!')