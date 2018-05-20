#!/usr/bin/python

"""
An exercise in playing with Exceptions.
Make lots of try/except blocks for fun and profit.

Make sure to catch specifically the error you find, rather than all errors.
"""

from except_test import fun, more_fun, last_fun


# Figure out what the exception is, catch it and while still
# in that catch block, try again with the second item in the list
first_try = ['spam', 'cheese', 'mr death']

try:
	joke = fun(first_try[0])
except NameError:
	print("that joke doesn't exist")

def display_the_joke(joke):
	print(joke)

# Here is a try/except block. Add an else that prints not_joke
try:
    not_joke = fun(first_try[2])
    display_the_joke(not_joke)

except SyntaxError:
    print('Run Away!')
else:
	print(not_joke)
	#finally runs whether there's an exception or not 
finally:
	print("This always runs")

print("after the exception block\n")

# What did that do? You can think of else in this context, as well as in
# loops as meaning: "else if nothing went wrong"
# (no breaks in  loops, no exceptions in try blocks)

# Figure out what the exception is, catch it and in that same block
#
# try calling the more_fun function with the 2nd language in the list,
# again assigning it to more_joke.
#
# If there are no exceptions, call the more_fun function with the last
# language in the list

# Finally, while still in the try/except block and regardless of whether
# there were any exceptions, call the function last_fun with no
# parameters. (pun intended)

langs = ['java', 'c', 'python']

def excepttest(x):
	try:
		print("Calling more_fun with",langs[x])
		more_joke = more_fun(langs[x])
		print(more_joke)
	except IndexError:
		print("IndexError exception was called")

for x in range(0,4):
	print("Calling function for",x,"\n")
	excepttest(x)