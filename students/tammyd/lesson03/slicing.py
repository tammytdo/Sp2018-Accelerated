a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)

#with the first and last items exchanged
def exchange_first_last(seq):
    return seq[-1:] + seq[1:-1] + seq[0:1]

print(exchange_first_last(a_string))
assert exchange_first_last(a_string) == "ghis is a strint"


#with every other item removed
def every_other_removed(seq):
    return seq[::2]

print(every_other_removed(a_tuple))
assert every_other_removed(a_tuple) == (2, 13, 5)


#with the first and last 4 items removed, and every other item in between
def rm_first_4_last_4(seq):
    return seq[1:-4:2]

print(rm_first_4_last_4(a_string))


#with the elements reversed (just with slicing).
def reversed(seq):
    return a_string[::-1]

print(reversed(a_string))


#with the last third, then first third, then the middle third in the new order.
def thirds(seq):
    total_chars = int(len(seq))
    third = int(total_chars) // 3
    first = seq[ :third]
    mid = seq[third: third *2]
    last = seq[third *2:]
    return last+" "+first+" "+mid

print(thirds(a_string))