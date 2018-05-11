#!/usr/bin/env python

# Series 1

fruits = ["Apples", "Pears", "Oranges", "Peaches"]

print("So far, you have {}\n".format(fruits))

fruits.append(input("Which fruit would you like to add? >> ").capitalize())
print("Now you have {}\n".format(fruits))

index = (int(input("Which index would you like to see? >> ")))
print("You requested fruit number {} which is {}\n".format(index, fruits[index - 1]))

fruits.insert(0, "Papaya")
print("A Papaya has been added to the beginning of the list!:\n", fruits)
print()

print("A surprising amount of fruits start with 'P' in this list:")
for fruit in fruits:
    if fruit[0] == 'P':
        print(fruit)
print()

# Series 2
# Display the list.
print("The fruit in your list so far are: {}".format(fruits))
# Remove the last fruit from the list.
del fruits[-1]
# Display the list.
print("Without that last addition you have: {}\n".format(fruits))

# Ask the user for a fruit to delete, find it and delete it.
# (Bonus: Multiply the list times two. Keep asking until a match is found. Once found, delete all occurrences.)
hated_fruit = input("Which fruit from the list would you like to delete? >> ").capitalize()

dupe_fruits = fruits * 2
dupe_fruits_new = []
for fruit in dupe_fruits:
    if fruit != hated_fruit:
        dupe_fruits_new.append(fruit)
print("Took care of that for you! Your list minus {} is now:".format(hated_fruit))
for fruit in dupe_fruits_new:
    print(fruit)
print()

# Series 3
# Again, using the list from series 1:
og_fruits = fruits[:]

# Ask the user for input displaying a line like “Do you like apples?” for each fruit in the list (making the fruit all lowercase).
for fruit in fruits:
    response = input("Do you like {}? Please answer Y/N >> ".format(fruit)).lower()
    # For each “no”, delete that fruit from the list.
    if response == "n":
        while fruit in fruits:
            fruits.remove(fruit)
    elif response == "y":
        pass
    else:
        # For any answer that is not “yes” or “no”, prompt the user to answer with one of those two values
        response = input("Please enter Y or N as a response this time! >> ")
print()
print("Here's a copy of your list with only the ones you like!")
# Display the list.
for fruit in fruits:
    print(fruit)
print()

# Series 4

# Make a copy of the list
fruits = og_fruits[:]
# reverse the letters in each fruit in the copy.
rev_fruit = []
for fruit in fruits:
    rev_fruit.append(fruit[::-1])
# Delete the last item of the original list.
del fruits[-1]
# Display the original list and the copy.
print("Your original list minus that last entry is: {}".format(fruits))
print("...and here they all are reversed!: {}".format(rev_fruit))
