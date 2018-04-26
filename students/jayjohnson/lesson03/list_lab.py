'''
Jay Johnson
list_lab
/////
Goal:
Learn the basic ins and outs of Python lists.

Hint
to query the user for info at the command line, you use:

response = input("a prompt for the user > ")
response will be a string of whatever the user types (until a <return>).

Procedure
In your student dir in the class repo, create a lesson03 dir and put in a new list_lab.py file.

Series 1
x Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
x Display the list (plain old print() is fine…).
x Ask the user for another fruit and add it to the end of the list.
x Display the list.
x Ask the user for a number and display the number back to the user and the fruit corresponding to that number (on a 1-is-first basis). Remember that Python uses zero-based indexing, so you will need to correct.
x Add another fruit to the beginning of the list using “+” and display the list.
x Add another fruit to the beginning of the list using insert() and display the list.
x Display all the fruits that begin with “P”, using a for loop.
Series 2
Using the list created in series 1 above:

x Display the list.
x Remove the last fruit from the list.
x Display the list.
x Ask the user for a fruit to delete, find it and delete it.
(Bonus: Multiply the list times two. Keep asking until a match is found. Once found, delete all occurrences.)
Series 3
Again, using the list from series 1:

x Ask the user for input displaying a line like “Do you like apples?” for each fruit in the list (making the fruit all lowercase).
x For each “no”, delete that fruit from the list.
x For any answer that is not “yes” or “no”, prompt the user to answer with one of those two values (a while loop is good here)
x Display the list.
Series 4
Once more, using the list from series 1:

Make a copy of the list and reverse the letters in each fruit in the copy.
Delete the last item of the original list. Display the original list and the copy.
'''
#!/usr/bin/env python3

#Series 1
#Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
fruit = ["Apples", "Pears", "Oranges","Peaches"]

#Display the list (plain old print() is fine…).
print(fruit)

#Ask the user for another fruit and add it to the end of the list.
new_fruit = input("Which fruit would you like to add? ")
fruit.append(new_fruit)
#Display the list.
print(fruit)

#Ask the user for a number and display the number back to the user and the fruit corresponding to that number
#(on a 1-is-first basis). Remember that Python uses zero-based indexing, so you will need to correct.
number = input("Number for fruit index please! (1 or above only)")

print("Your number selection is: " + number)
print("Your fruit index is: " + fruit[int(number)-1])

#Add another fruit to the beginning of the list using “+” and display the list.
new_fruit_front = input("Which fruit would you like to add to the beginning? ")
fruit = [new_fruit_front] + fruit
print(fruit)

#Add another fruit to the beginning of the list using insert() and display the list.
new_fruit_insert = input("Which fruit would you like to add to the beginning? ")
fruit.insert(0,new_fruit_insert)
print(fruit)

lower_case = []
lower_case = [fruit.lower() for fruit in fruit]
print(lower_case)

#Display all the fruits that begin with “P”, using a for loop.
newList = []

for word in lower_case:
    if word.startswith('p'):
        newList.append(word)

print(newList)

#Display the list.
print(fruit)

#Remove the last fruit from the list.
fruit = fruit[:-1]
#Display the list.
print(fruit)

#deletion = input("What fruit would you like to delete?: ")

#Ask the user for a fruit to delete, find it and delete it.
#fruit.remove(deletion)

print(fruit)

lower_case = []
lower_case = [fruit.lower() for fruit in fruit]
#print(lower_case)

#Ask the user for input displaying a line like “Do you like apples?”
#for each fruit in the list (making the fruit all lowercase).
#For each “no”, delete that fruit from the list.
#For any answer that is not “yes” or “no”, prompt the user to answer
#with one of those two values (a while loop is good here)
for i in range(len(lower_case)):
    while True:
        print("Do you like " + lower_case[i] + "?")

        answer = input("")

        if answer not in ("no", "yes"):
            print("Not a Valid response -- type no or yes")
            continue
        elif answer == "no":
            fruit.remove(fruit[i])
            break
        elif answer == "yes":
            print()
            break

#Display the list.
print(fruit)

#Make a copy of the list and
fruit_copy = []
fruit_copy = fruit
#reverse the letters in each fruit in the copy.
for i in range(len(fruit_copy)):
    fruit_copy[i] = fruit_copy[i][::-1]

print(fruit_copy)

fruit_copy_new = []
fruit_copy_new = fruit
#Delete the last item of the original list.
fruit_copy_new = fruit[:-1]
#Display the original list and the copy.
print(fruit)
print(fruit_copy_new)
