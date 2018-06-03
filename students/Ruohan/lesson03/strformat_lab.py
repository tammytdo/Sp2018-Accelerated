#! /usr/bin/env python3


#taks one and two
print('=====task one and task two======')

def task_one(a_tuple):
    new = 'file_{:0>3d}:, {:.2f}, {:.2e}, {:.2e}'.format(*a_tuple)
    return new
a_tuple = (2, 123.4567, 10000, 12345.67)
print(task_one(a_tuple))



#task theree
print('=============task three===============')
def formatter(in_tuple):
    q = len(in_tuple) - 1
    numbers = '{:d},' * q + '{:d}'
    form_string = f'the {q} numbers are: {numbers}'
    return form_string.format(*in_tuple)
in_tuple = (2,3,4,5)
print(formatter(in_tuple))
#taks four
print('=============task four==================')
def task_four(tuple):
    new_str = '{3:0>2d},{4},{2},{0:0>2d},{1}'.format(*tuple)
    return new_str
another_tuple = (4, 30, 2017, 2, 27)
print(task_four(another_tuple))
#task five
print('==============task five=================')

def task_five(e_list,w = 1):
    li_new =f'The wight of an {e_list[0][:-1].upper()} is {e_list[1] * w} and the weight of a {e_list[2][:-1].upper()} is {e_list[-1]*w}'
    return li_new
e_list = ['oranges', 1.3, 'lemons', 1.1]
print(task_five(e_list))
print(task_five(e_list, 1.2))

#task six
print('==============task six=================')
def task_six(tuple):
    table = 'name:{:10}, age:{:8}, cost: {:8}'.format(*tuple)
    return table
tuple6 = ('Ruohan','28','$300')
tuple7 = ('David', '23','$6789')
print(task_six(tuple6))
print(task_six(tuple7))
