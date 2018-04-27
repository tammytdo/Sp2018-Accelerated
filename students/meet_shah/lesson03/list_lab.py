#!/usr/bin/env python3

fruits = ["Apples", "Pears", "Oranges", "Peaches"]
def series1(fruits):
    print("***Begin Series 1***")
    print(fruits)
    response = input("Please enter the name of a fruit>>")
    fruits.append(response)
    print(fruits)
    while True:
        new_response = int(input("Please enter a number for which fruit display>>"))
        if len(fruits) < new_response:
            print("Your response, {}, is out of index. Please try again".format(new_response))
        else:
            print("Item number {} in list is: {}".format(new_response, fruits[new_response - 1]))
            break
    fruits = ["Berries"] + fruits
    print(fruits)
    fruits.insert(4, "Crans")
    print(fruits)
    for fruit in fruits:
        if "p" in fruit[0].lower():
            print(fruit)

def series2(fruits):
    print("***Begin Series 2***")
    print(fruits)
    fruits = fruits[:-1]
    print(fruits)
    response = input("Please enter the name of a fruit to delete>>")
    fruits = [fruit for fruit in fruits if fruit != response]
    print(fruits)
    print("Series2: Bonus round")
    fruits = fruits * 2
    print(fruits)
    while True:
        response = input("Please enter the name of a fruit to delete>>")
        new_fruits = [fruit for fruit in fruits if response != fruit]
        print(new_fruits)
        if len(new_fruits) != len(fruits):
            fruits = new_fruits
            break
    print(fruits)

def series3(fruits):
    print("***Begin Series 3***")
    print(fruits)
    new_fruits = []
    for fruit in fruits:
        response = input("Do you like {} >>".format(fruit.lower()))
        if response != 'no':
            new_fruits.append(fruit)
    fruits = new_fruits
    print(fruits)

def series4(fruits):
    print("***Begin Series 4***")
    new_fruits = []
    for fruit in fruits:
        new_fruits.append(fruit[::-1])
    print(new_fruits)
    fruits = fruits[:-1]
    print(fruits)


series1(fruits)
print(fruits)
series2(fruits)
print(fruits)
series3(fruits)
print(fruits)
series4(fruits)
print(fruits)
