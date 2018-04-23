#!/usr/bin/env python3

# Series 1
# Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']

# Display the list (plain old print() is fine…).
print(fruits)

# Ask the user for another fruit and add it to the end of the list.
add_fruit = input('Enter another type of fruit > ')

fruits.append(add_fruit)

# Display the list.
print(fruits)

# Ask the user for a number and display the number back to the user and
# the fruit corresponding to that number (on a 1-is-first basis). Remember
# that Python uses zero-based indexing, so you will need to correct.

fruit_index = input('Pick a number between 1 and {:d} > '.format(len(fruits)))

print('You entered {}:'.format(fruit_index))

print(fruits[int(fruit_index) - 1])

# Add another fruit to the beginning of the list using “+” and display the list.
fruits = ['Bananas'] + fruits

print(fruits)

# Add another fruit to the beginning of the list using insert() and display the list.

fruits.insert(0, 'Grapes')

print(fruits)

# Display all the fruits that begin with “P”, using a for loop.
for fruit in fruits:
    if 'P' in fruit:
        print(fruit)

# Series 2
# Using the list created in series 1 above:
# Display the list.
print(fruits)

# Remove the last fruit from the list.
del fruits[-1:]

# Display the list.
print(fruits)

# Ask the user for a fruit to delete, find it and delete it.
del_fruit = input('What fruit do you want to delete from the list? ')

fruits.remove(del_fruit)

print(fruits)

# (Bonus: Multiply the list times two. Keep asking until a match is found. Once found, delete all occurrences.)

fruits.append(del_fruit) # Added deleted fruit back into the list

print(fruits)

fruits = fruits * 2

print(fruits)

del_fruit = input('Pick a fruit to delete from the list > ')

while del_fruit not in fruits:
    del_fruit = input("That fruit isn't in the list. Enter another fruit to delete > ")

while del_fruit in fruits:
    fruits.remove(del_fruit)

print(fruits)

# Series 3
# Again, using the list from series 1:

fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']

# Ask the user for input displaying a line like “Do you like apples?” for each fruit in the list (making the fruit all lowercase).
# For each “no”, delete that fruit from the list.
# For any answer that is not “yes” or “no”, prompt the user to answer with one of those two values (a while loop is good here)
# Display the list.

for fruit in fruits[:]: # iterate over a copy of the sequence you want to mutate
    response = input('Do you like {}? '.format(fruit.lower()))
    while response not in ['yes', 'Yes', 'Y', 'y', 'no', 'No', 'N', 'n']:
        print('Invalid response. Please enter "yes" or "no".')
        response = input('Do you like {}? '.format(fruit.lower()))
    if response in ['no', 'No', 'N', 'n']:
        fruits.remove(fruit) # mutate the list

print('Fruits you like:')
print(fruits)

# Series 4
# Once more, using the list from series 1:
fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
# Make a copy of the list and reverse the letters in each fruit in the copy.
copy_fruits = fruits[:]

for fruit in copy_fruits[:]:
    copy_fruits.remove(fruit)
    copy_fruits.append(fruit[-1:].upper() + fruit[:-1][::-1].lower())

# Delete the last item of the original list. Display the original list and the copy.

del fruits[-1:]

print(fruits)
print(copy_fruits)