a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)

def exchange_first_last(seq):
    mylist = list(seq)
    mylist[0],mylist[len(mylist)-1] = mylist[len(mylist)-1], mylist[0]
    if type(seq) == str:
        seq = ''.join(mylist)
    if type(seq) == tuple:
        seq = tuple(mylist)
    return seq


assert exchange_first_last(a_string) == "ghis is a strint"
assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)

