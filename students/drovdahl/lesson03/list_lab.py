#! /usr/local/bin/python3


'''
Modify a series of lists using a number of functions
'''
import os
list1 = ['Apples', 'Pears', 'Oranges', 'Peaches']


def series1():
    print('Here is the current list of fruits:', '\n\n', list1, '\n')
    response = input('Enter a new fruit to add to the list >>')
    list1.append(response)
    print('\nHere is an updated list of fruit\n\n', list1, '\n')
    response = int(input('Enter the number of one of the fruits (starting with'
                         ' 1)\n >>'))
    print(list1[response - 1])


if __name__ == "__main__":
    os.system('clear')
    series1()
