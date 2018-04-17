#! /usr/local/bin/python3


def generate_name_error():
    x = y
# name error because the 'y' variable has not been defined


def generate_type_error():
    x = 2 + '2'
# type error due to inconsistent variable types being used in this equation


# def generate_syntax_error():
    # print('hello)
    # syntax error due to string not being contained in pair of single quotes


def generate_attribute_error():
    mylist = ['a', 'b', 'c']
    print(mylist)
    mylist.apppend('d')
# attribute error due to typo in the 'append' attribute.  There is no attribute called 'apppend'


# generate_name_error()
# generate_type_error()
# generate_syntax_error()
# generate_attribute_error()
