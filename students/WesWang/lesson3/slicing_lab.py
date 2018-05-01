#=========================================================================================
#Name: Slicing Lab
#Author: Wesley Wang
#Date: 4/18/2018
#=========================================================================================

# Exchange first and last items
def exchange_first_last(seq):
  result = [seq[-1]] + seq[1:-1] + [seq[0]]
  return result

# Remove every other item
def remove_every_other(seq):
  result = seq[::2]
  return result

# Remove first and last four items, and every other item in between
def trim_four_every_other(seq):
  result = seq[4:-4:2]
  return result

# Reverse order of items with slicing
def reverse(seq):
  result = seq[::-1]
  return result

#
def mid_last_first(seq):
    first_third = len(seq)//3
    second_third = (len(seq)//3)*2
    result = seq[first_third:second_third] + seq[second_third:] + seq[:first_third]
    return result

a_string = "This is a string"
a_tuple = [1,2,3,4,5,6,7,8,9,10,11,12]

assert exchange_first_last(a_string) == "ghis is a strinT"
assert exchange_first_last(a_tuple) == [12,2,3,4,5,6,7,8,9,10,11,1]
