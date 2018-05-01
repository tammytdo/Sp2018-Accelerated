#!/usr/bin/env python


def fruitfunc():
    print("SERIES 1:")
    fruitlist1 = ['Apples', 'Pears', 'Oranges', 'Peaches']
    print(fruitlist1)
    print()

# Ask user for a fruit and adds it to an existing list(append)
    newfruit = input("What fruit would you like to add? ")
    fruitlist1.append(newfruit)
    print(fruitlist1)
    print()

# Ask user for a number returns that number and the fruit associated with it
# indexing
    fruitindex = eval(input("Enter a number to display fruit: "))
    print(fruitindex, fruitlist1[fruitindex - 1])
    print()

# Ask user for a fruit and adds it to an existing list(concatenation of two
# lists
    fruitlist1 = ['Apples', 'Pears', 'Oranges', 'Peaches']
    onelist = []
    newfruit3 = input("What fruit would you like to add? ")
    onelist.append(newfruit3)
    newlist = fruitlist1 + onelist
    print(newlist)
    print()

# Ask user for a fruit and adds it to an existing list(insert) at the start
# of the list
    newfruit2 = input("What fruit would you like to add? ")
    fruitlist1.insert(0, newfruit2)
    print(fruitlist1)

# prints all the fruit in the list that start with P
    print()
    fruitlist1 = ['Apples', 'Pears', 'Oranges', 'Peaches']
    Pfruit = []
    for item in fruitlist1:
        if "P" in item:
            Pfruit.append(item)
    print("Fruits that begin with 'P'")
    print(Pfruit)
    print()

    print("SERIES 2:")
# Uses pop to remove the last item in the list.
    fruitlist1 = ['Apples', 'Pears', 'Oranges', 'Peaches']
    print(fruitlist1)
    poppedfruit = fruitlist1.pop()
    print("Fruit removed: ")
    print(poppedfruit)
    print("Fruit List after removal")
    print(fruitlist1)

# asks uses which item they want removed, uses pop and index to
# remove that item
    print()
    fruitlist1 = ['Apples', 'Pears', 'Oranges', 'Peaches']
    print(fruitlist1)
    rm_fruit = input("Which fruit do you want removed from the list? ")
    for item in fruitlist1:
        if rm_fruit == item:
            fruitindex = (fruitlist1.index(rm_fruit))
            fruitlist1.pop(fruitindex)
    print("Fruit List after removal")
    print(fruitlist1)
    print()

    print("SERIES 3:")
# if user does not like a certain fruit, remove it from list.  could not
# figure out how to re-ask the same question after an answer that was not
# 'no' or 'yes'
    fruitlist1 = ['Apples', 'Pears', 'Oranges', 'Peaches']
    for item in reversed(fruitlist1[:]):
        GoodWillHunting = input(("Do you like {}? ").format(item))
        if GoodWillHunting != 'no' and GoodWillHunting != 'yes':
            print("Please enter 'yes' or 'no' only.")
        elif GoodWillHunting == "no":
            fruitindex = (fruitlist1.index(item))
            fruitlist1.pop(fruitindex)
    print(fruitlist1)
    print()

    print("SERIES 4:")
# print the fruit list in the proper order but print each word in reverse
    fruitlist1 = ['Apples', 'Pears', 'Oranges', 'Peaches']
    fruitcopy = fruitlist1.copy()
    print(fruitcopy)
    revfruitlistSer4Copy = []
    for item in fruitcopy:
        revfruitlistSer4Copy.append(item[::-1])
    print(revfruitlistSer4Copy)


fruitfunc()