#! /usr/bin/env python3

''' simple mailroom proram for a non profit'''

import sys

datas = [['William Gates, III',  653784.39, 2],['Mark Zuckerberg', 16396.10, 3],
        ['Jeff Bezos', 877.33, 1],['Paul Allen', 708.42, 3]]

names = []
for data in datas:
    names.append(data[0])
def thank_you():
    item = input("Enter donor's name: ")
    if items == 'list':
        print(names)
    elif items not in names:
        names.appen(item)
    else:


    else:
        for i in datas:
            if item == i[0]


def report():
    print('This is the report function')

def quit():
    sys.exit()

def mainloop():
    print('welcome to Mailroom')

    response = ''
    while True:
        print('what do you want to do?')
        print('1) than you\n'
              '2) report\n'
              '3) quit\n')
        response = input('>> ')

        if response not in ('1', '2', '3'):
            print('***Not a valid response -- type 1,2,3***\n')
            continue
        elif response == '1':
            thank_you()
        elif response == '2':
            report()
        elif response == '3':
            quit()



if __name__ == '__main__':
#     mail()
