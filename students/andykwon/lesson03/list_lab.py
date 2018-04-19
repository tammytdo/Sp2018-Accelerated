#!/usr/bin/env python3

# Series 1
fruit = ["Apples", "Pears", "Oranges", "Peaches"]

print(fruit)

print("Please enter a fruit name")
response = input(">")

fruit.append(response)

print(fruit)

# Request a number, display the item in the list that corresponds to the list
print("Please enter a number")
response = input(">")

print(fruit[int(response) - 1])

# Adding a fruit to the front of the list using the + operand
fruit = ["Banana"] + fruit

print(fruit)

# Adding a fruit to the front of the list using the insert method
fruit.insert(0, "Mango")

print(fruit)

print("fruits that only start with P:")

# Printing fruits in the list that start with "P"
for i in range (len(fruit)):
    if fruit[i][0] == "P":

        print(fruit[i])