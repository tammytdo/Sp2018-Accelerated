#! /usr/local/bin/python3


'''
simple mail program for non profit
'''

import sys
import os

donors = [('Iron Man', [100000, 50000, 1000]),
          ('Thor', [50, 25, 100]),
          ('Hulk', [500]),
          ('Captain America', [30, 40]),
          ('Nick Fury', [100000, 545, 1000]),
          ('Hawkeye', [75, 50, 20]),
          ('Black Panther', [1000, 900, 50]),
          ('War Machine', [10, 10])
          ]


def thankyou():
    '''
    Function which will allow user to type 'list' to see a list of donors.
    The user can also add a new donation to either an existing donor or a
    brand new donor.
    The global list 'donors' will be modified with any new donors and/or
    donations.
    Once a new donation has been made, a THANK YOU email will be printed to the
    screen.
    '''
    global donors
    print('''So, you just recieved a new donation.  That's great!

Let's record the donation and draft a THANK YOU message.


Who is the donor? Type the name of the donor or type 'list' to see a
list of existing donors.
(type 'quit' at any time to return to the main menu)''')
# collect the donor name
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
# collect the donation amount
    donor_donation = input('What is the donation amount? \n >> ')
# normallize the donation amount
    donor_donation = donor_donation.replace('$', '').replace(',', '')
    donor_donation = float(donor_donation)
# iterate through the donors list to see if the donor already exists
# if the donor already exists, append the new donation amount to the existing
# list
# if the donor is not matched, add a new donor/donation amount entry to the
# donors list
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
    '''
    This report will print a list of donors, total donated, number of
    donations,, and average donation amounts as values in each row.
    Using string formatting, the output rows will line up as nice as possible.
    The end result will be tabular (values in each column should align with
    those above and below)
    '''
    os.system('clear')
    # print top row
    print('Donor Name                | Total Given | Num Gifts | Average Gift',
          '\n' + ('-' * 66))
    # length of first cell
    a1 = ' ' * 28
    # length of second and forth cell
    a2 = ' ' * 11
    # length of third cell(first half)
    a3_1 = ' ' * 7
    # length of third cell(second half)
    a3_2 = ' ' * 7
    # length of forth cell
    # a5 = ' ' * 11
    for x in donors:
        donor = x[0]
        gift_total = round(sum(x[1]), 2)
        gift_number = len(x[1])
        gift_average = round((sum(x[1])/len(x[1])), 2)
        # assign the output of the first cell
        c1 = donor + a1[len(donor):]
        # assign the value of the second cell
        c2 = '$' + a2[0:-(len(str(gift_total)))] + str(gift_total)
        # assign the value of the third cell
        c3 = a3_1[0:-(len(str(gift_number)))] + str(gift_number) + a3_2
        # assign the value of the forth cell
        c4 = '$' + a2[0:-(len(str(gift_average)))] + str(gift_average)
        # print the row
        print(c1 + c2 + c3 + c4)
    print('\n\n')


def quit():
    sys.exit()


def mainloop():
    '''
    Main menu function
    '''
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
        if response not in ('1', '2', '3', 'quit'):
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
        elif response == '3' or 'quit':
            quit()


if __name__ == "__main__":
    mainloop()
