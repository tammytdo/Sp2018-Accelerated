def exchange_first_and_last(seq):
    print("this is exchange_first_and_last")

    return seq[-1:] + seq[1:-1] + seq[:1]

    # first = seq[:1]
    # last = seq[-1:]
    # middle = seq[1:-1]

    # return first + last + middle

def every_other_removed(seq):
    print("this is every_other_removed")

    return seq[::2]

def remove_first_last_four_and_every_other(seq):
    print("this is remove_first_last_four_and_every_other")

    seq = seq[4:]
    seq = seq[:-4]
    seq = seq[::2]

    return seq

def elements_reversed_slicing(seq):
    print("this is elements_reversed_slicing")

    return seq[::-1]

def reorder_middle_last_first_third(seq):
    print("this is reorder_middle_last_first_third")

    first_third = seq[:int(len(seq)/3)]
    middle_third = seq[int(len(seq)/3):int(len(seq)/3) * 2]
    last_third = seq[int(len(seq)/3) * 2:]

    reordered = middle_third + last_third + first_third

    return reordered

a_string = "Good eye might"
a_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)

assert exchange_first_and_last(a_string) == "tood eye mighG"
assert exchange_first_and_last(a_tuple) == (12, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 1)

assert every_other_removed(a_string) == "Go y ih"
assert every_other_removed(a_tuple) == (1, 3, 5, 7, 9, 11)

assert remove_first_last_four_and_every_other(a_string) == " y "
assert remove_first_last_four_and_every_other(a_tuple) == (5, 7)

assert elements_reversed_slicing(a_string) == "thgim eye dooG"
assert elements_reversed_slicing(a_tuple) == (12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1)

assert reorder_middle_last_first_third(a_string) == " eye mightGood"
assert reorder_middle_last_first_third(a_tuple) == (5, 6, 7, 8, 9, 10, 11, 12, 1, 2, 3, 4)

print("all good!")

# print(exchange_first_and_last(a_string))
# print(exchange_first_and_last(a_tuple))

# print(every_other_removed(a_string))
# print(every_other_removed(a_tuple))

# print(remove_first_last_four_and_every_other(a_string))
# print(remove_first_last_four_and_every_other(a_tuple))

# print(elements_reversed_slicing(a_string))
# print(elements_reversed_slicing(a_tuple))

# print(reorder_middle_last_first_third(a_string))
# print(reorder_middle_last_first_third(a_tuple))
