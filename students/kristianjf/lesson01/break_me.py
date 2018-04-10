def break_me_name():
    #Break Name Error
    x = y

def break_me_type():
    #Break Type Error
    x = int(test)

#Break Syntax Error
#dict(x:y)


def break_me_attribute():
    test = {}
    test.__getattribute__('x')
    #Break Attribute Error

break_me_name()
break_me_type()
dict(x:y)
break_me_attribute()
