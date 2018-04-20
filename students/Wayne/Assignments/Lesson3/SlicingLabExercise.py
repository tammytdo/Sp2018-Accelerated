# Slicing Lab Exercise


# a_string = "this is a string"
# a_tuple = (2, 54, 13, 12, 5, 32)

# assert exchange_first_last(a_string) == "ghis is a strint"
# assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)

# with the first and last items exchanged.

def exchange_first_last(a_string):
    a_string = input()
    a_tuple = 'taco'
    return (a_string[-1:] + a_string[1:-1] + a_string[:1])
    a_string[-1] + a_string[1:-1] + a_string[0]
    tuple[-1:] + a_tuple[1:-1] + a_tuple[:1]

assert exchange_first_last ('This is a string') == "ghis is a strint"

print('exchange_first_last passed assert test')



# with every other item removed.


# with the first and last 4 items removed, and every other item in between.


# with the elements reversed (just with slicing).


# with the middle third, then last third, then the first third
# in the new order.
