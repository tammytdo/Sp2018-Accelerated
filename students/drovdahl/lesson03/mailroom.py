#! /usr/local/bin/python3


'''
simple mail program for non profit
'''

import sys
import os

donors = [('Iron Man', [1000000, 5000000, 10000000]),
          ('Thor', [50, 25, 100]),
          ('Hulk', [500]),
          ('Captain America', [30, 40]),
          ('Nick Fury', [100000, 545, 1000]),
          ('Hawkeye', [75, 50, 20]),
          ('Black Panther', [1000, 900, 50]),
          ('War Machine', [10, 10])
          ]


def thankyou():
    print('this is the thankyou function\n')


def report():
    print('this is the reporting function\n')


def quit():
    sys.exit()


def mainloop():
    os.system('clear')
    print('''Avengers - Fund a kitten initiative
  Because every little girl
  Everywhere in the world
  ...deserves a kitten

Welcome to Mailroom\n''')
    while True:
        print('What do you want to do?')
        print('1 - thank you\n'
              '2 - report\n'
              '3 - quit')
        response = input('>> ')
        if response not in ('1', '2', '3'):
            os.system('clear')
            print('not a valid repsonse, type "1, 2, or 3"\n')
            continue
        elif response == '1':
            os.system('clear')
            thankyou()
            continue
        elif response == '2':
            os.system('clear')
            report()
            continue
        elif response == '3':
            quit()


if __name__ == "__main__":
    mainloop()
