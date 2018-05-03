# List Lab Exercise

# Link to http://www.upriss.org.uk/python/session5.html


# SERIES 1

# Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
# Display the list (plain old print() is fine…).
# Ask the user for another fruit and add it to the end of the list.
# Display the list.
# Ask the user for a number and display the number back to the user and the fruit
# corresponding to that number (on a 1-is-first basis). Remember that Python uses
# zero-based indexing, so you will need to correct.
# Add another fruit to the beginning of the list using “+” and display the list.
# Add another fruit to the beginning of the list using insert() and display the list.
# Display all the fruits that begin with “P”, using a for loop.


lst = ['Apples', 'Pears', 'Orange']
lstadd = input("Enter a new fruit").strip()
lst.append(lstadd)
numberoffruit = int(input('What is the quanity of fruit?'
                          ' 1 = Apple'
                          ' 2 = Pears'
                          ' 3 = Orange'
                          ' 4 = {}'.format(lstadd)).strip())
print(lst[numberoffruit - 1])

lst = ['Banana'] + lst

print(lst)

for fruit in lst:
    if fruit[0].lower() == 'p':
        print(fruit)


# SERIES 2

# Using the list created in series 1 above:

# Display the list.
# Remove the last fruit from the list.
# Display the list.
# Ask the user for a fruit to delete, find it and delete it.
# (Bonus: Multiply the list times two. Keep asking until a match is found. Once found,
# delete all occurrences.)

print(lst)

"""
.pop() the last part of the list
"""

lst.pop()

print(lst)

deleteafruit = input('Which fuit do you want to '
                     'remove from the list?')

lst.remove(deleteafruit)

print(lst)


# Series 3

# Again, using the list from series 1:

# Ask the user for input displaying a line like “Do you like apples?” for each fruit in
# the list (making the fruit all lowercase).
# For each “no”, delete that fruit from the list.
# For any answer that is not “yes” or “no”, prompt the user to answer with one of those
# two values (a while loop is good here)
# Display the list.

newlst = []

for fruit in lst:
    fruitpreference = input("do you like this fruit? {}".format(fruit))
    if fruitpreference != 'no' and fruitpreference != 'yes':
        print(fruitpreference)
        print("Not a Valid Entry, input yes or no")
    elif fruitpreference == 'yes':
        newlst.append(fruit)


# Series 4

# Once more, using the list from series 1:

# Make a copy of the list and reverse the letters in each fruit in the copy.
# Delete the last item of the original list. Display the original list and the copy


reverselst = newlst[::-1]

print(reverselst)

deletelastlst = lst[:-1]

print(deletelastlst)
