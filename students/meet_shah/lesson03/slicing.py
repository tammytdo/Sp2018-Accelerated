a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)

def exchange_first_last(seq):
   first = seq[0]
   middle = seq[1:len(seq)-1]
   last = seq[-1]
   newseq = last + middle + first
   return newseq

print(exchange_first_last(a_string))

assert exchange_first_last(a_string) == "ghis is a strint"
assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)

