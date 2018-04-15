
# Activity:
# Write four simple Python functions:
# Each function, when called, should cause an exception to happen
# Each function should result in one of the four most common exceptions you’ll find.
# For review: NameError, TypeError, SyntaxError, AttributeError

# NameError
def generate_nameerror():
    n = m

#generate_nameerror()

# TypeError
def generate_typeerror():
    x = 3
    y = 'three'
    x / y

#generate_typeerror()

# SyntaxError
#def generate_syntaxerror():
#    0 = 10

#generate_syntaxerror()

# AttributeError
def generate_attributeerror():
    s = 27
    s.len()

generate_attributeerror()