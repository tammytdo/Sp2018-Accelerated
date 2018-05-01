# Slicing Lab Exercise


a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)


# with the first and last items exchanged.


def exchange_first_last(a_string):
    new_string= input()
    return new_string[-1] + new_string[1:-1] + new_string[0]
    print(a_string)


# assert exchange_first_last('This is a string') == "ghis is a strint"

# print('exchange_first_last passed assert test')

# with every other item removed.

everyotherstr = a_string[1::2]

print(everyotherstr)

# with the first and last 4 items removed, and every other item in between.

frstlstfoureveryother = a_string[-4] + a_string[1::2] + a_string[:4]

print(frstlstfoureveryother)

# with the elements reversed (just with slicing).

reversestr = a_string[::-1]

print(reversestr)

# with the middle third, then last third, then the first third
# in the new order.
