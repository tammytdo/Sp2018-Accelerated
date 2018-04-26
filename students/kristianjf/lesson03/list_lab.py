#!/usr/bin/env python3
'''
Series 1
Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
'''
FRUITS = ['Apples', 'Pears', 'Oranges', 'Peaches']
'''
Display the list (plain old print() is fine…).
'''
print('\nList of Fruits:\n', FRUITS)
def add_fruit(lst):
    '''
    Ask the user for another fruit and add it to the end of the list.
    '''
    return lst.append(input('Would y ou like to add a fruit to the list?: '))
add_fruit(FRUITS)
'''
Display the list.
'''
print('\nList of Fruits:\n', FRUITS)
def select(lst):
    '''
    Ask the user for a number and display the number back to the user and the fruit
    corresponding to that number (on a 1-is-first basis).
    '''
    fruit_list = [x for x in enumerate(lst, 1)]
    fruit_index = [str(x[0]) for x in fruit_list]
    response = ''
    while response not in fruit_index:
        response = input('Select a number from {} to {}: '.format(fruit_index[0], fruit_index[-1]))
        return fruit_list[int(response)-1] if response in fruit_index else select(lst)

print(select(FRUITS))
'''
Add another fruit to the beginning of the list using “+” and display the list.
'''
FRUITS = ['Bananas'] + FRUITS
print('\nList of Fruits:\n', FRUITS)
'''
Add another fruit to the beginning of the list using insert() and display the list.
'''
FRUITS.insert(0, 'Mangos')
print('\nList of Fruits:\n', FRUITS)
'''
Display all the FRUITS that begin with “P”, using a for loop.
'''
for x in FRUITS:
    if x.startswith('P'):
        print(x)

FRUITS_S1 = FRUITS[:]
'''
Series 2
Using the list created in series 1 above:

Display the list.
Remove the last fruit from the list.
'''
FRUITS = FRUITS_S1[:]
print('\nList of Fruits:\n', FRUITS)
FRUITS.pop()

'''
Display the list.
'''
print('\nList of Fruits:\n', FRUITS)

def remove_fruit(lst):
    '''
    Ask the user for a fruit to delete, find it and delete it.
    '''
    response = input('Select a fruit to remove from the list: ')
    lst += lst
    if response in lst:
        lst = set(lst)
        lst.remove(response)
        return list(lst)
    else:
        print(f'The fruit you have selected is not in the list. Please try again\n{list(set(lst))}')
        return remove_fruit(list(set(lst)))

FRUITS = remove_fruit(FRUITS)
print('\nList of Fruits:\n', FRUITS)


FRUITS = FRUITS_S1[:]
def liked_fruits(lst):
    '''
    Series 3
    Again, using the list from series 1:

    Ask the user for input displaying a line like “Do you like apples?”
    for each fruit in the list (making the fruit all lowercase).
    For each “no”, delete that fruit from the list.
    For any answer that is not “yes” or “no”, prompt the user to answer
    with one of those two values (a while loop is good here)
    Display the list.
    '''
    for fruit in lst[:]:
        response = ''
        while response not in ['yes', 'no']:
            print(f'Do you like {fruit}?\n Please select yes or no')
            response = input()
        if response == 'no':
            lst.remove(fruit)
    return lst

print('\nList of Fruits:\n', FRUITS)
FRUITS = liked_fruits(FRUITS)
print('\nList of Fruits:\n', FRUITS)


FRUITS = FRUITS_S1[:]
def rev_fruit(lst):
    '''
    Series 4
    Once more, using the list from series 1:

    Make a copy of the list and reverse the letters in each fruit in the copy.
    '''
    new_list = [x[::-1] for x in lst[:]]
    return new_list

FRUITS_S4 = rev_fruit(FRUITS)
'''
Delete the last item of the original list. Display the original list and the copy.
'''
FRUITS.pop()
print('\n', FRUITS, '\n', FRUITS_S4)
