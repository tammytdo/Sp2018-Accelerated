#! /usr/local/bin/python3


'''
lesson04 activity

Dictionaries Part 1
1.  Create a dictionary containing “name”, “city”, and “cake” for “Chris” from
    “Seattle” who likes “Chocolate” (so the keys should be: “name”, etc, and
    values: “Chris”, etc.)
2.  Display the dictionary.
3.  Delete the entry for “cake”.
4.  Display the dictionary.
5.  Add an entry for “fruit” with “Mango” and display the dictionary.
     Display the dictionary keys.
     Display the dictionary values.
     Display whether or not “cake” is a key in the dictionary (i.e. False)(now)
     Display whether or not “Mango” is a value in the dictionary (i.e. True)
Dictionaries Part 2
1.  Using the dictionary from item 1: Make a dictionary using the same keys but
    with the number of ‘t’s in each value as the value (consider upper and
    lower case?).
Sets Part 1
1.  Create sets s2, s3 and s4 that contain numbers from zero through twenty,
    divisible by 2, 3 and 4.
2.  Display the sets.
3.  Display if s3 is a subset of s2 (False)
    and if s4 is a subset of s2 (True).
Sets Part 2
1.  Create a set with the letters in ‘Python’ and add ‘i’ to the set.
2.  Create a frozenset with the letters in ‘marathon’.
3.  Display the union and intersection of the two sets.
'''
d1 = {}
d2 = {}
s2 = set()
s3 = set()
s4 = set()

def dict_1():
    # create the dict and add values
    print('Function - dict_1')
    global d1
    d1.update({'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'})
    print(d1)
    # remove the entry for 'cake'
    del d1['cake']
    print(d1)
    # add entry for fruit
    d1.update({'fruit': 'Mango'})
    print(d1)
    # display the dictionary keys
    print(d1.keys())
    # display the dictionary values
    print(d1.values())
    # check for key - 'cake'
    print('Is \'cake\' in d1? : ' + str('cake' in d1))
    # check for 'Mango'
    print('Is \'Mango\' a value in d1? : ' + str('Mango' in d1.values()) + '\n')
    return


def dict_2():
    # create new dict from d1 and modify values
    print('Function - dict_2')
    global d1
    global d2
    # iterate over d1 and populate d2 with identical keys but d2 values should
    # be assigned the number of 't's that are contained in the d1 values
    # example - Seattle = '2'
    for key in d1.keys():
        t_count = 0
        t_count = d1.get(key).lower().count('t')
        d2.setdefault(key, t_count)
    print(d2, '\n')

    return


def set_1():
    # create sets s2, s3, s4 and add values based on divisibility of 2, 3, 4
    print('Function - set_1')
    global s2, s3, s4
    for x in range(21):
        if x % 2 == 0:
            s2.update([x])
        if x % 3 == 0:
            s3.update([x])
        if x % 4 == 0:
            s4.update([x])
    print('s2 =', s2)
    print('s3 =', s3)
    print('s4 =', s4)
    # is s3 a subset of s2 (False)
    print('s3 is subset of s2:', s3.issubset(s2))
    # is s4 a subset of s2 (True)
    print('s4 is subset of s2:', s4.issubset(s2), '\n')
    return


def set_2():
    # create a set with the letters in 'Python' and add 'i' to the set
    print('Function - set_2')
    s = set(['P', 'y', 't', 'h', 'o', 'n'])
    s.update('i')
    print(s)
    # create frozenset with letters in 'marathon'
    s_frozen = frozenset(['m', 'a', 'r', 'a', 't', 'h', 'o', 'n'])
    print(s_frozen)
    # display union and intersection of both sets
    print('union =', s.union(s_frozen))
    print('intersection =', s.intersection(s_frozen))
    return


if __name__ == "__main__":
    dict_1()
    dict_2()
    set_1()
    set_2()
