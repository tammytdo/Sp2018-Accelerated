# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 20:08:21 2018

@author: mattn
"""

# Dictionaries 1

"""
- (x) Create a dictionary containing “name”, “city”, and “cake” for “Chris” from “Seattle” who likes “Chocolate” (so the keys should be: “name”, etc, and values: “Chris”, etc.)
- (x) Display the dictionary.
- (x) Delete the entry for “cake”.
- (x) Display the dictionary.
- (x) Add an entry for “fruit” with “Mango” and display the dictionary.
- (x) Display the dictionary keys.
- (x) Display the dictionary values.
- (x) Display whether or not “cake” is a key in the dictionary (i.e. False) (now).
- (x) Display whether or not “Mango” is a value in the dictionary (i.e. True).

"""

import os
    
dict_red = {'name' : 'Chris', 'cake' : 'Chocolate', 'city' : 'Seattle'}

dict_red

for i, k in dict_red.items():
    print("%s %s" % (i,k))

dict_red.pop('cake')

def bar():
    '''
    displays a line of 68 '*'
    '''
    print()
    for i in range(68):
        print("*", end="")
    print()

def pg_br():
    '''
    adds a couple of line feeds for human easy reading
    '''
    print()
    print()
    
def io_cake():
    """
    checks if 'cake' is still in the dictionary
    """
    cake_status = 'cake' in dict_red.keys()
    print(cake_status)
    
def io_mango():
    """
    checks if 'mango' is still in the dictionary
    """
    mango_status = 'Mango' in dict_red.values()
    print(mango_status)
    
pg_br()
print("Really liked that cake!")
print("Pop! it's gone.", end="")
pg_br()
    
for i, k in dict_red.items():
    print("%s %s" % (i,k))
    
dict_red['fruit'] = 'Mango'

bar()


print("Some fruit instead? Mango perhaps?")
pg_br()
    
for i, k in dict_red.items():
    print("%s %s" % (i,k))

bar()

for i in dict_red.keys():
    print(i)

bar()

for i in dict_red.values():
    print(i)

bar()

print("True or False: Is the 'cake' still in our dictionary?")
    
io_cake()
bar()

print("True or False: Is the 'Mango' still in our dictionary?")
io_mango()

# Dictionaries 2
"""
- (x) Using the dictionary from item 1: Make a dictionary using the same keys but 
with the number of ‘t’s in each value as the value (consider upper and lower case?).

*****   Got stuck- used CEB solution for dict 2 but add .lower() method
"""

a_dict = {}
for key, val in dict_red.items():
    a_dict[key] = val.lower().count('t')
print(a_dict)

bar()

# Sets 1
"""
- (x) Create sets s2, s3 and s4 that contain numbers from zero through twenty, 
    divisible by 2, 3 and 4.
- (x) Display the sets.
- (x) Display if s3 is a subset of s2 (False)
- (x) and if s4 is a subset of s2 (True).
"""

s2 = set()
s3 = set()
s4 = set()

for i in range(21):
    if not i % 2:
        s2.add(i)
    if not i % 3:
        s3.add(i)
    if not i % 4:
        s4.add(i)

print(s2)
print(s3)
print(s4)

bar()

print("Is set s3 a subset of set s2?")
print(s3.issubset(s2))

bar()

print("Is set s4 a subset of set s2?")
print(s4.issubset(s2))

bar()

# Sets 2
"""
- (x) Create a set with the letters in ‘Python’ and add ‘i’ to the set.
- (x) Create a frozenset with the letters in ‘marathon’.
- (x) display the union and intersection of the two sets.
"""

p = set('python')
p.add('i')
print(p)

bar()

f = frozenset('marathon')
print('union', p.union(f))
print('intersection', p.intersection(f))

bar()

# Activity 2: File Lab

'''
Paths and File Processing
- (x) Write a program which prints the full path for all files in the current 
    directory, one per line
- (x) Write a program which copies a file from a source, to a destination 
    (without using shutil, or the OS copy command).
- () Advanced: make it work for any size file: i.e. don’t read the entire 
    contents of the file into memory at once.
- () This should work for any kind of file, so you need to open the files in 
    binary mode: open(filename, 'rb') (or 'wb' for writing). Note that for 
    binary files, you can’t use readline() – lines don’t have any meaning for 
    binary files.
- () Test it with both text and binary files (maybe jpeg or something of your chosing).
'''
bar()
print("Listing the names of all the files in the current directory")
print()

for i in os.listdir():
    print(i)

bar()
print()
print("Copying 'test_file01.txt from current directory to parent directory ./mathewcm/result_file01.txt")

with open('test_file01.txt', 'rb') as infile, open('D:\\uw\\Sp2018-Accelerated\\students\\mathewcm\\result_file01.txt', 'wb') as outfile:
    outfile.write(infile.read())
    
bar()


    
    
    

    












