#! /usr/local/bin/python3


'''
simple mail program for non profit
'''

import sys
import os
import pathlib

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
    os.system('clear')
    print('''So, you just recieved a new donation.  That's great!

Let's record the donation and draft a THANK YOU message.


Who is the donor? Type the name of the donor or type 'list' to see a list of
existing donors.  (type 'quit' at any time to return to the main menu)''')
# collect the donor name
    donor = input(' >> ')
    if donor.lower() == 'quit':
        return
    while donor.lower() == 'list':
        os.system('clear')
        print('Here\'s a list of our generous donors:\n  ', end='')
        print(*[x[0] for x in donors], sep='\n  ')
        print('Type the name of an existing or new donor.\n'
              '(type "quit" at any time to return to the main menu)')
        donor = input(' >> ')
        if donor.lower() == 'quit':
            return
    # collect the donation amount
    donor_donation = input('What is the donation amount? \n >> ')
    # normallize the donation amount
    donor_donation = donor_donation.replace('$', '').replace(',', '')
    donor_donation = float(donor_donation)
    # iterate through the donors list to see if the donor already exists
    # if the donor already exists, append the new donation amount to the
    # existing list
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
    # compute the number of donated kittens at $5.00 per kitten with a matching
    # donation of * 2
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
    global donors
    os.system('clear')
    # print top row
    a = 'Donor Name'
    b = 'Total Given'
    c = 'Num Gifts'
    d = 'Average Gift'
    print(f'{a: <20}|{b:^13}|{c:^13}|{d:^15}')
    # print bar
    a = b = c = d = '-'
    print(f'{a:-<20}-{b:-<13}-{c:-<13}-{d:-<15}')
    # print donor specific rows
    for x in donors:
        a = x[0]
        b = round(sum(x[1]), 2)
        c = len(x[1])
        d = round((sum(x[1])/len(x[1])), 2)
        print(f'{a: <20} ${b: >12} {c:^13} ${d: >14}')
    print('\n\n')
    return


def letters_to_all():
    '''
    Function to go through all the donors and generate a thank you letter that
    will be written to disk as a text file in the 'letters' directory.
    The letter files will all have unique names and include time/date stamps in
    the file name.
    '''
    global donors
    os.system('clear')
    # create 'letters' directory if one does not exist
    pathlib.Path('letters').mkdir(exist_ok=True)
    # iterate over donors data and create files for each donor
    for x in donors:
        donor = x[0]
        donations = round(sum(x[1]), 2)
        letter_text = f'Hi there {donor}!\n\nThanks for the ${donations:,}'
        # set the file path using pathlib
        p = pathlib.Path('letters/' + donor)
        with open(p, 'w') as outfile:
            outfile.write(letter_text)
    print('All the letters have been composed and can be found in the '
          '\'letters\' directory\n\n')
    return


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

Welcome to Mailroom\n\n''')
    switch_func_dict = {'1': thankyou, '2': report, '4': quit, 'quit': quit,
                        '3': letters_to_all}
    while True:
        print('Choose an action:\n')
        print('1 - Send a THANK YOU\n'
              '2 - Create a report\n'
              '3 - Send letters to everyone\n'
              '4 - Quit')
        response = input(' >> ')
        if switch_func_dict.get(response) is None:
            os.system('clear')
            print('not a valid repsonse, type "1, 2, or 3"\n')
        else:
            switch_func_dict.get(response)()


if __name__ == "__main__":
    mainloop()
