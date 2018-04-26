
'''
This program is hard-coded of defined specifications to
create a grid.  The same grid will be printed everytime the
program is ran.

'''

# defines variable used in the body of the functions
plus = "+"
minus = "-"
space = " "
post = "|"
block = (space + minus + space + minus + space +
         minus + space + minus + space)


# function that creates the top line
def topmidbot():
    print(plus + block + plus + block + plus)


# function that creates the box walls
def postline():
    print(post + space * 9 + post + space * 9 + post)
    print(post + space * 9 + post + space * 9 + post)
    print(post + space * 9 + post + space * 9 + post)
    print(post + space * 9 + post + space * 9 + post)


# calls the functions
topmidbot()
postline()
topmidbot()
postline()
topmidbot()
