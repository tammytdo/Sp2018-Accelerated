a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)
a_list = [3,4,5,6,7,8]
def exchange_first_last(seq):
   return seq[-1:] + seq[1:-1] + seq[:1]

assert exchange_first_last(a_list) == [8,4,5,6,7,3]
assert exchange_first_last(a_string) == "ghis is a strint"
assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)

