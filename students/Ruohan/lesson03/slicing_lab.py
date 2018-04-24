'''fuctions of slicing exercise'''

a_string = 'this is Ruohan'
a_tuple = (12, 34, 44, 27, 56, 4, 19)


def exchange_first_last(seq):
    ''' return sequence with the first and last items exchanged'''
    a_new_sequence = seq[-1:] + seq[1:-1] + seq[:1]
    return a_new_sequence

assert exchange_first_last(a_string) == 'nhis is Ruohat'
assert exchange_first_last(a_tuple) == (19, 34, 44, 27, 56, 4, 12)



def every_other_removed(seq):
    '''return sequence with other item removed'''
    a_new_sequence = seq[::2]
    return a_new_sequence
assert every_other_removed(a_string) == 'ti sRoa'
assert every_other_removed(a_tuple) == (12, 44, 56, 19)


def first_last4_removed(seq):
    '''return sequence with the first and last 4 items removed,
    and every other item in between'''
    a_new_sequence = seq[1:-4]
    return a_new_sequence
assert first_last4_removed(a_string) == 'his is Ru'
assert first_last4_removed(a_tuple) == (34, 44)


def reversed_sequrece(seq):
    '''return sequence with the elements reversed'''
    return seq[::-1]
assert reversed_sequrece(a_string) == 'nahouR si siht'
assert reversed_sequrece(a_tuple) == (19, 4, 56, 27, 44, 34, 12)


def new_order(seq):
    '''return sequence with the third last third,
    then the first third, then the middle third in the new order'''
    idx = len(seq)//3
    return seq[-idx:]+seq[:idx]+seq[idx:-idx]

assert new_order(a_string) == 'ohanthis is Ru'
assert new_order(a_tuple) == (4, 19, 12, 34, 44, 27, 56)
