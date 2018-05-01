!/usr/bin/env python3

def task1(t):
    return "file_{:03}: {:.02f}, {:.2e}, {:.3e}".format(*t)

assert task1((2, 123.4567, 10000, 12345.67)) == 'file_002: 123.46, 1.00e+04, 1.235e+04'

def task2(t):
    return t

def task3(t):
    return ("the {} numbers are: "+ ", ".join(["{:d}"]*len(t))).format(len(t), *t)

assert(task3((1,2,3))) == "the 3 numbers are: 1, 2, 3"
assert(task3((3,4,5,6,7))) == "the 5 numbers are: 3, 4, 5, 6, 7"

def task4(t):
    return ("{:02} {:02} {:02} {:02} {:02}").format(t[3],t[4],t[2],t[0],t[1])

assert task4((4, 30, 2017, 2, 27)) == "02 27 2017 04 30"

def task5(t):
    return f'The weight of an {t[0]} is {t[1]} and the weight of a {t[2]} is {t[3]}'

assert task5(['oranges', 1.3, 'lemons', 1.1]) == "The weight of an oranges is 1.3 and the weight of a lemons is 1.1"


def task6(t):
    return '{:20}{:>6}{:>25}'.format(*t)

print(task6(('Name', 'Age', 'Cost')))
print(task6(('Hello', '10', '200')))
print(task6(('Yello', '50', '4000')))
print(task6(('Bello', '100', '50000')))
