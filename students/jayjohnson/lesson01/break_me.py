'''
Jay Johnson lesson01

In the break_me.py file write four simple Python functions:

Each function, when called, should cause an exception to happen
Each function should result in one of the four most common exceptions you’ll find.
for review: NameError, TypeError, SyntaxError, AttributeError
(hint – the interpreter will quit when it hits a Exception
– so you can comment out all but the one you are testing at the moment)

'''

# error functions
def nameError_fuction():
    a = 5
    del a
    a

def typeError_fuction():
    type = 'abc'
    type('efg')

def syntaxError_fuction():
    #del = 'error please'

def AttributeError_fuction():
    pass

# will need to comment out all others to get thewe to fail correctly
nameError_fuction()

typeError_fuction()

syntaxError_fuction()

AttributeError_fuction(error)
