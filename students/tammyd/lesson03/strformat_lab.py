#!/usr/bin/env python3

'''
String Formatting Lab Exercise
'''

#take the following four element tuple: ( 2, 123.4567, 10000, 12345.67)
t =  (2, 123.4567, 10000, 12345.67)
#print("My string =", t)
print("Goal: file_002 :   123.46, 1.00e+04, 1.23e+04")
print()

#Task one
#and produce: 'file_002 :   123.46, 1.00e+04, 1.23e+04'
print("Task one") 
print("This is file_{:03d} : {:8.2f}, {:.2e}, {:.3g}".format(2, 123.4567, 10000, 12345.67))
print()

#Task Two
#Using your results from Task One, repeat the exercise using an alternate type of format string
print("Task two") 
print(f"This is file_{t[0]:003d}: {t[1]:.2f}, {t[2]:.2e}, {t[3]:.3g}.".format(t))
print()


#Task Three
#Dynamically Building up Format Strings
#Rewrite: "the 3 numbers are: {:d}, {:d}, {:d}".format(1,2,3)
print("Task three")
t2 = (1, 2, 3, 4, 5, 6)
l = len(t2)
formatter = "The {} numbers are: ".format(l)
print(formatter + ", ".join(['{}']*l).format(*t2))


#Put your code in a function
def formatter(in_tuple):
    l = len(in_tuple)
    formatter = "The {} numbers are: ".format(l)
    formatter_arbitrary = (formatter + ", ".join(['{}']*l).format(*in_tuple))
    return formatter_arbitrary

print()
print("Task three in function")
print(formatter(t2))
print()

#Task Four
#use index numbers to specify positions
print("Task four")
print("Output: '02 27 2017 04 30'")
t4 = (4, 30, 2017, 2, 27)
print("{3:02d}, {4}, {2}, {0:02d}, {1}".format(*t4))



#Task Five
lst = ['oranges', 1.3, 'lemons', 1.1]
print(f"The weight of an {lst[0][:-1]} is {lst[1]} and the weight of a {lst[2][:-1]} is {lst[3]}.")
print(f"The weight of an {lst[0][:-1].upper()} is {lst[1]*1.2} and the weight of a {lst[2][:-1].upper()} is {lst[3]*1.2}.")


#Task six
print('{:20}{:10}{:20}{:8}'.format('First', '$99.01', 'Second', '$88.09'))

data = [('abc', 10, 100),
        ('def', 20, 2000),
        ('hij', 30, 30000),
        ('klm', 40, 400000),
        ('mno', 50, 5000000),
        ('pqr', 60, 60000000)
        ]


for name, age, cost in data:
    table = f'Name: {name:<10} Age: {age:<10} Cost: {cost:<10,.2f}'
    print(table)



#Bonus
#print the tuple in columns that are 5 charaters wide
t10 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10) 
print(('{:<5}'*len(t10)).format(*t10))
