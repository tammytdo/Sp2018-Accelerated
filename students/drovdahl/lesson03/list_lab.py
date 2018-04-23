#! /usr/local/bin/python3


'''
Modify a series of lists using a number of functions
'''
import os
list0 = ['Apples', 'Pears', 'Oranges', 'Peaches']
lists1 = []
lists2 = []
lists3 = []
lists4 = []


def series1():
    global list0
    global lists1
    lists1 = list0[:]
    print('Starting Series 1\n'
          'Here is the current list of fruits:', '\n\n', lists1, '\n')
    # add a fruit to the end of the list
    response = input('Enter a new fruit to add to the list >>')
    lists1.append(response)
    print('\nHere is an updated list of fruit\n\n', lists1, '\n')
    # print the fruit corresponding to the item number the user enters
    response = int(input('Enter the number of one of the fruits (starting with'
                         ' 1)\n >>'))
    print(response, lists1[response - 1])
    response = input("Hit 'Enter' to continue >>")
    os.system('clear')
    print('Here is the current list of fruits:', '\n\n', lists1, '\n')
    # add another fruit to the beginning of the list using the '+' method
    response = input('Enter a fruit to add to the beginning of the list >>')
    lists1 = [response] + lists1
    os.system('clear')
    print('Here is the current list of fruits:', '\n\n', lists1, '\n')
    # add another fruit to the beginning of the list using the insert() method
    response = input('Enter a fruit to add to the beginning of the list >>')
    lists1.insert(0, response)
    os.system('clear')
    print('Here is the current list of fruits:', '\n\n', lists1, '\n')
    # Display all the fruits that begin with 'p' using a for loop
    print('All these fruits start with a \'P\'')
    for word in lists1:
        for letter in word[0]:
            if word[0].lower() == 'p':
                print(word)
    response = input("Hit 'Enter' to continue >>")
    return


def series2():
    global lists1
    global lists2
    lists2 = lists1[:]
    os.system('clear')
    print('Starting Series 2\n'
          'Here is the current list of fruits:', '\n\n', lists1, '\n\n')
    # removing the last fruit from the list
    print('Now removing the last fruit from the list...\n\n')
    del lists2[-1]
    print('Here is the new list of fruits:', '\n\n', lists2, '\n')
    response = input("Hit 'Enter' to continue >>")
    # ask user for fruit to delete
    os.system('clear')
    while lists2 != []:
        print('Here is the current list of fruits:', '\n\n', lists2, '\n')
        lists2_copy = lists2[:]
        response = input('Type a fruit to delete it >>')
        i = 0
        for fruit in lists2:
            if response.lower() == fruit.lower():
                del lists2[i]
                print(response, 'removed...')
                response = input("Hit 'Enter' to continue >>")
                os.system('clear')
                break
            else:
                i += 1
        if lists2_copy == lists2:
            print('uh oh...\n  you did not pick a valid fruit and now you will'
                  ' be punished\n')
            lists2 = lists2 + lists2
            response = input("Hit 'Enter' to continue >>")
            os.system('clear')
    print('Congratulations!\nYou have successfully removed all the fruit\n\n')
    response = input("Hit 'Enter' to continue >>")
    return


def series3():
    global list0
    global lists3
    lists3 = list0[:]
    os.system('clear')
    print('Starting Series 3\n'
          'Here is the current list of fruits:', '\n\n', lists3, '\n\n')
    # remove fruit the user doesn't like
    lists3_copy = lists3[:]
    for fruit in lists3_copy:
        i = lists3.index(fruit)
        response = input(f'do you like {fruit}?\n  >>')
        if response.lower() == 'no':
            del lists3[i]
    os.system('clear')
    print('You\'re a picky eater!!\n'
          'Here is a new list with all the fruit you like\n\n', lists3, '\n\n')
    response = input("Hit 'Enter' to continue >>")
    return


def series4():
    global list0
    global lists4
    lists4 = list0[:]
    os.system('clear')
    print('Starting Series 4\n'
          'Here is the current list of fruits:\n\n', lists4, '\n\n')
    lists4_copy = []
    for fruit in lists4:
        lists4_copy.append(fruit[::-1])
    print('We\'ve just reversed the letters in every fruit in your list...\n')
    response = input("Hit 'Enter' to continue >>")
    os.system('clear')
    print('Here is the current list of fruits with backwards letters:\n\n',
          lists4_copy, '\n\n')
    del lists4[-1]
    print('Lastly - Here\'s the original list with the last item deleted:\n',
          lists4, '\n\nNow go eat some pizza...')
    return


if __name__ == "__main__":
    os.system('clear')
    series1()
    series2()
    series3()
    series4()
