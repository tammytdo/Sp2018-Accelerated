#! /usr/bin/env python3
'''Exercise about list'''
#series 1
#Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
#Display the list
print('============= series 1 ===============')
list_fruit = ['Apples', 'Pears', 'Oranges', 'Peaches']
print(list_fruit)

#Ask the user for another fruit and add it to the end of the list.
#Display the list.
item = input('Enter another fruit: ')
list_fruit.append(item)
print(list_fruit)

#Ask the user for a number and display the number back to the user
#and the fruit corresponding to that number
x = int(input('Enter the number: '))
print(x, list_fruit[x-1])

#Add another fruit to the beginning of the list using “+” and display the list.
item_new = input('Enter another fruit: ')
list_fruit_new = [item_new] + list_fruit
print(list_fruit_new)

#Add another fruit to the beginning of the list using insert() and display the list.
item = input('Enter another fruit: ')
list_fruit_new.insert(0, item)
print('====original list: ', list_fruit_new, '=====')


#Display all the fruits that begin with “P”, using a for loop.
for ft in list_fruit_new:
    if ft[0] == 'P':
        print(ft)

#Series 2
#Display the list.
print('============= series 2 ===============')
list_fruit_2 = list_fruit_new[:]
print(list_fruit_2)

#Remove the last fruit from the list and display the list
list_fruit_2.pop()
print(list_fruit_2)

#Ask the user for a fruit to delete, find it and delete it.
tgt = input('Enter the fruit you want to delete: ')
idx = list_fruit_2.index(tgt)
list_fruit_2.pop(idx)
print(list_fruit_2)


#Series 3
#Ask the user if he likes the fruit for each fruit in the list and display the list
print('============= series 3 ===============')
list_fruit_3 = list_fruit_new[:]
for fruit in list_fruit_new:
    y = input('Do you likes {} ? '.format(fruit.lower()))
    while True:
        if y == 'no':
            list_fruit_3.pop(list_fruit_3.index(fruit))
            break
        if y == 'yes':
            break
        else:
            y = input("invalid argument, please enter 'yes'or 'no': ")
print(list_fruit_3)

#Series 4
#Make a copy of the list and reverse the letters in each fruit in the copy.
print('============= series 4 ===============')
list_fruit_4 = []
for fruit in list_fruit_new:
    fruit = fruit[::-1]
    list_fruit_4.append(fruit)
print(list_fruit_4)

#Delete the last item of the original list. Display the original list and the copy.
list_fruit_new.pop()
list_fruit_4 = list_fruit_new[:]
print('original list: ', list_fruit_new)
print('new list: ', list_fruit_4)
