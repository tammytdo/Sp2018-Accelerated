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




