#NameError:
def give_NameError():
    print ('NameError: ')
    print (y)

#TypeError
def give_TypeError():
    print ('TypeError: ')
    x = 2
    y = 'hello'
    print(x+y)


# SyntaxError
def give_SyntaxError():
    print ('SyntaxError: ')
    x = and
    print(x)


#AttributeError
def give_AttributeError():
    print('AttributeError: ')
    A = {1,3,5,7,9}
    B = A.split()
    
