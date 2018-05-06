#! /usr/local/bin/python3


'''
simple mail program for non profit
'''

import sys
import os
import pathlib
import datetime

donors = [('Iron Man', [100000, 50000, 1000]),
          ('Thor', [50, 25, 100]),
          ('Hulk', [500]),
          ('Captain America', [30, 40]),
          ('Nick Fury', [100000, 545, 1000]),
          ('Hawkeye', [75, 50, 20]),
          ('Black Panther', [1000, 900, 50]),
          ('War Machine', [10, 10])
          ]
donors_dict = dict(donors)


def thankyou_menu():
    '''submenu for the THANK YOU function'''
    switch_func_dict = {'1': add_donation_user_input, '2': print_donors_list,
                        'list': print_donors_list, '3': 1, 'quit': 1}
    while True:
        os.system('clear')
        print('''THANK YOU Menu

Let's record that new donation and draft a THANK YOU message.\n\n''')
        print('\nChoose an action:\n')
        print('1 - Enter the name of a donor\n'
              '2 - Enter "list" to see a list of existing donors\n'
              '3 - Enter "quit" to return to the main menu\n')
        response = input(' >> ')
        if switch_func_dict.get(response) is None:
            os.system('clear')
            print('not a valid repsonse, try again\n')
        elif switch_func_dict.get(response) is 1:
            os.system('clear')
            print('MAIN Menu')
            return
        else:
            switch_func_dict.get(response)()


def print_donors_list():
    os.system('clear')
    print('Here\'s a list of our generous donors:\n')
    print(*(x for x in donors_dict), sep='\n')
    input('\n  press "Enter" to return to the THANK YOU Menu ')
    return


def add_donation_user_input():
    '''Function to collect user input for donor and donation_amount values'''
    print('\nType the name of an existing or new donor.\n'
          '(type "quit" at any time to return to the main menu)')
    donor = input(' >> ')
    if donor.lower() == 'quit':
        return
    donor_donation = input('What is the donation amount? \n >> ')
    # normallize the donation amount
    donor_donation = donor_donation.replace('$', '').replace(',', '')
    try:
        donor_donation = float(donor_donation)
    except ValueError:
        print('\nNot a valid entry.  Need to enter a numerical value for the '
              'donation amount\n')
        input('  press "Enter" to return to the THANK YOU Menu ')
        return
    add_donation(donor, donor_donation)
    print_thankyou_letter(donor, donor_donation)
    return


def add_donation(donor, donor_donation):
    '''Update donor if they exist or add new donor and donation amount'''
    donors_dict.setdefault(donor, []).append(donor_donation)
    return


def print_thankyou_letter(donor, donor_donation):
    os.system('clear')
    print('Below is an email tailored to this donor...\n\n')
    print(thankyou_letter(donor, donor_donation))
    input('\n  press "Enter" to return to the THANK YOU Menu ')
    return


def thankyou_letter(donor, donor_donation):
    '''Returns a THANK YOU letter'''
    # compute the number of donated kittens at $5.00 per kitten with a matching
    # donation of * 2
    k = (donor_donation/5 * 2)
    letter = (f'''Dear {donor},
        We at the Avengers Fund-a-Kitten Initiative would like to thank you for
    your generous donation of ${donor_donation:,.2f}.\n
    Taking advantage of our kitten matching partner, with these added funds we
    will be able to provide {k:,.2f} kitten(s) to well deserving little girls
    all over the world including hard to reach places like Antarctica and
    Tacoma, WA!\n\n
        Sincerely,
        Your Friends at AFAK
    ''')
    return letter


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
    a = 'Donor Name'
    b = 'Total Given'
    c = 'Num Gifts'
    d = 'Average Gift'
    print(f'{a: <20}|{b:^13}|{c:^13}|{d:^15}')
    # print bar
    a = b = c = d = '-'
    print(f'{a:-<20}-{b:-<13}-{c:-<13}-{d:-<15}')
    # print donor specific rows
    for a in donors_dict:
        b = round(sum(donors_dict.get(a)), 2)
        c = len(donors_dict.get(a))
        d = round(b / c, 2)
        print(f'{a: <20} ${b: >12,.2f} {c:^13} ${d: >14,.2f}')
    input('\n\n\n  press "Enter" to return to the THANK YOU Menu ')
    os.system('clear')
    print('MAIN Menu')
    return


def letters_to_all():
    '''
    Function to go through all the donors and generate a thank you letter that
    will be written to disk as a text file in the 'letters' directory.
    The letter files will all have unique names and include time/date stamps in
    the file name.
    '''
    os.system('clear')
    # create 'letters' directory if one does not exist
    pathlib.Path('letters').mkdir(exist_ok=True)
    # set the datetime format variable
    dt_format = '.%m-%d-%Y'
    # iterate over donors data and create files for each donor
    for donor in donors_dict:
        donor_donations = round(sum(donors_dict.get(donor)), 2)
        letter_text = thankyou_letter(donor, donor_donations)
        # set the file path using pathlib
        p = pathlib.Path('letters/' + donor +
                         datetime.datetime.now().strftime(dt_format) + '.txt')
        with open(p, 'w') as outfile:
            outfile.write(letter_text)
    print('All the letters have been composed and can be found in the '
          '\'letters\' directory\n\n')
    input('\n\n\n  press "Enter" to return to the THANK YOU Menu ')
    os.system('clear')
    print('MAIN Menu')
    return


def quit():
    sys.exit()


def mainloop():
    '''main menu function'''
    os.system('clear')
    print('''Avengers: Fund-a-Kitten Initiative

  Because every little girl
  Everywhere in the world
  ...deserves a kitten


Welcome to Mailroom\n\n''')
    switch_func_dict = {'1': thankyou_menu, '2': report, '4': quit,
                        'quit': quit, '3': letters_to_all}
    while True:
        print('\nChoose an action:\n')
        print('1 - Send a THANK YOU\n'
              '2 - Create a report\n'
              '3 - Send letters to everyone\n'
              '4 - Quit')
        response = input('\n >> ')
        if switch_func_dict.get(response) is None:
            print('not a valid repsonse, type "1, 2, 3, or 4"\n')
        else:
            switch_func_dict.get(response)()


if __name__ == "__main__":
    mainloop()
