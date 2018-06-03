a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)
a_list = [3,4,5,6,7,8]
another_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
def exchange_first_last(seq):
   return seq[-1:] + seq[1:-1] + seq[:1]

##Validations##
assert exchange_first_last(a_list) == [8,4,5,6,7,3]
assert exchange_first_last(a_string) == "ghis is a strint"
assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)

def every_other_item(seq):
   return seq[::2]

assert every_other_item(a_list) == [3, 5, 7]
assert every_other_item(a_string) == "ti sasrn"
assert every_other_item(a_tuple) == (2, 13, 5)

def first_last_four_every_other_removed(seq):
   myitem = seq[4:-4]
   return myitem[::2]

assert first_last_four_every_other_removed(a_list) == []
assert first_last_four_every_other_removed(another_list) == [5,7,9]
assert first_last_four_every_other_removed(a_string) == " sas"

def reversed(seq):
   return seq[::-1]

assert reversed(a_list) == [8,7,6,5,4,3]
assert reversed(a_string) == "gnirts a si siht"

def last_first_middle(seq):
   third = len(seq)//3
   ##          last    +   first      +    middle
   return seq[-third:] + seq[:third]  + seq[third:-third]

assert last_first_middle(a_list) == [7,8,3,4,5,6]
assert last_first_middle(a_string) == "tringthis is a s"


