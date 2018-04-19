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
    global donors
    print('So, you just recieved a new donation.  That\'s great!')
    print('Let\'s record the donation and draft a THANK YOU message\n')
    print('Who is the donor? Type the name of the donor or "list" to see a'
          'list of existing donors.\n(type "quit" at any time to return to the'
          'main menu)')
    donor = input('>> ')
    if donor.lower() == 'quit':
        return
    while donor.lower() == 'list':
        os.system('clear')
        print('Here\'s a list of our generous donors:\n  ', end='')
        print(*[x[0] for x in donors], sep='\n  ')
        print('Type the name of an existing or new donor.\n'
              '(type "quit" at any time to return to the main menu)')
        donor = input('>> ')
        if donor.lower() == 'quit':
            return
    donor_donation = input('What is the donation amount? \n >> ')
    donor_donation = donor_donation.replace('$', '').replace(',', '')
    donor_donation = float(donor_donation)
#    print('%.2f' % donor_donation)
    x = 0
    name_match = False
    for name in donors:
        if name[0] == donor:
            donors[x][1].append(donor_donation)
            name_match = True
        x += 1
    if name_match is False:
        donors.append((donor, [donor_donation]))
# compose a THANK YOU email
    os.system('clear')
    k = (donor_donation/5 * 2)
    print('Below is an email tailored to this donor...\n\n')
    print(f'''Dear {donor},
        We at the Avengers Fund-a-Kitten Initiative would like to thank you for
    your generous donation of $%.2f.\n
    Taking advantage of our kitten matching partner, with these added funds we
    will be able to provide {k} kitten(s) to well deserving little girls all
    over the world including hard to reach places like Antacrtica and
    Tacoma, WA!\n\n
        Sincerely,
        Your Friends at AFAK
    ''' % donor_donation)


def report():
    print('this is the reporting function\n')


def quit():
    sys.exit()


def mainloop():
    os.system('clear')
    print('''Avengers: Fund-a-Kitten Initiative
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
