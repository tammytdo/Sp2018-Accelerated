#!/usr/bin/env python3
'''
Jay Johnson
Comprehensions Lab
'''

feast = ['lambs', 'sloths', 'orangutans',
             'breakfast cereals', 'fruit bats']

comprehension = [delicacy.capitalize() for delicacy in feast]

print(comprehension[0])
# lambs
# correct

print(comprehension[2])
# Orangutans
# correct

feast = ['spam', 'sloths', 'orangutans', 'breakfast cereals',
            'fruit bats']

comp = [delicacy for delicacy in feast if len(delicacy) > 6]

print(len(feast))
# will print how many items are in feast so 5
# correct

print(len(comp))
# will print how many items are in comp so 3
#correct

eggs = ['poached egg', 'fried egg']

meats = ['lite spam', 'ham spam', 'fried spam']

comprehension = \
[ '{0} and {1}'.format(egg, meat) for egg in eggs for meat in meats]

print(len(comprehension))
# will print out how many items there are. 2 groups of 3 so 6
# correct

print(comprehension[0])
# poached egg and lite spam
# correct

list_of_tuples = [(1, 'lumberjack'), (2, 'inquisition'), (4, 'spam')]

comprehension = [ skit * number for number, skit in list_of_tuples ]

print(comprehension[0])
# lumberjack
# correct

print(len(comprehension[2]))
# spamspamspamspam so 16
# correct

comprehension = { c for c in 'aabbbcccc'}

print(comprehension)
# cccc
# wrong
# the c variable throws you off Here
# for any letter that repeats add it to Comprehensions
# {'c', 'b', 'a'}


dict_of_weapons = {'first': 'fear',
                       'second': 'surprise',
                       'third':'ruthless efficiency',
                       'forth':'fanatical devotion',
                       'fifth': None}
dict_comprehension = \
{ k.upper(): weapon for k, weapon in dict_of_weapons.items() if weapon}


print('first' in dict_comprehension)
# fear
# wrong
# False
# not sure why this is returning False
# i see its because it turned everything to upper case so
# first wasn't == to FIRST


print('FIRST' in dict_comprehension)
# should return true
# correct

print(len(dict_of_weapons))
# 10
# wrong its 5
# each key and value only counts as one instead of 2


print(len(dict_comprehension))
# not sure how this returns 4
