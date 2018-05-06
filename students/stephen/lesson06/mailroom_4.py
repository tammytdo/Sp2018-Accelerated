#!/usr/bin/env python

"""
Simple Mailroom Program for a nonprofit
"""

# The script should prompt the user (you) to choose from a menu of 3 actions:
# “Send a Thank You”, “Create a Report” or “quit”)

# Interactive Loop
import sys

# Create a data object to store donor information
donors = {
    'Jeff Bezos': [50, 100, 56],
    'Mark Zuckerberg': [45, 105, 349, 101, 78],
    'Paul Allen': [10, 50, 400, 400],
    'Elon Musk': [16, 68, 170, 425],
    'Richard Branson': [25, 90, 124, 300]
}

def gen_letter(donor):
    """
    Takes the donor iterable and returns a string that is a formatted thank you note
    with the donor's name and last donation amount.
    """
    return "Dear {:s},\n\nWe greatly appreciate your generous donation of ${:,.2f}.\n\nThank you,\nThe Team".format(donor[0], donor[1])

def filename(name):
    'Return a txt file name based on the donor name and using underscores instead of spaces'
    return name.replace(' ', '_') + '.txt'

def write_letters_to_disk(dict=donors):
    """
    Generate one letter for each donor and write to disk
    """
    for n, d in dict.items():
        print('Generating letter to {:s}'.format(n))
        donor = (n, d[-1])
        letter = gen_letter(donor)
        with open(filename(n), 'w') as outfile:
            outfile.write(letter)
    print()
    return

def add_donation(name, amount, dict=donors):
    return dict.setdefault(name, []).append(amount)

def enter_name(name, amount):
    ex = 0
    while ex == 0:
        try:
            amount = float(amount)
        except ValueError:
            print('Please enter a valid amount')
            amount = input('>> ')
            continue
        else:
            ex = 1
    add_donation(name, amount)
    print(gen_letter([name, amount]))
    print()

def get_name_donation():
    print('\nEnter the full name of the donor:')
    ty_name = input('>> ')
    print('Enter a donation amount:')
    ty_amount = input('>> ')
    print()
    enter_name(ty_name, ty_amount)

def donor_list():
    print('\nDonors:')
    for name in donors:
        print(name)
    print()

def thank_you():
    print()
    print('You have chosen Send a Thank You')
    ty_choice = ''
    switch_func_dict = {
        '1': get_name_donation,
        '2': donor_list
    }
    while ty_choice != '3':
        print('1) Enter the full name of the recipient\n2) See a list of donor names\n3) Return to the Main Menu')
        ty_choice = input('>> ')
        try:
            switch_func_dict.get(ty_choice)()
        except TypeError:
            print('Not a valid response. Type 1, 2, or 3\n')
        continue
    return
        

def avg_donations(donations):
    return sum(donations[1]) / len(donations[1])

def sum_donations(donations):
    return sum(donations[1])

def report_data(dict=donors):
    sorted_donors = list(dict.items())
    sorted_donors.sort(key=sum_donations, reverse=True)
    report_rows = []
    for d in sorted_donors:
        report_rows.append('{:26s} {:>12s} {:^13d} {:>12s}\n'.format(d[0], ('${:,.2f}'.format(sum(d[1]))), len(d[1]), ('${:,.2f}'.format(avg_donations(d)))))
    return ''.join(report_rows)

def report():
    print('Donor Name                | Total Given | Num Gifts | Average Gift')
    print('-' * 66)
    print(report_data())
    return

def quit():
    sys.exit()

def mainloop():
    print('Welcome to Mailroom')
    response = ''
    switch_dict = {
        '1': thank_you,
        '2': report,
        '3': write_letters_to_disk,
        '4': quit
    }
    while response != '4':
        print('What do you want to do?')
        print('1) Send a Thank You\n2) Create a Report\n3) Send letters to everyone\n4) Quit')
        response = input('>> ')
        # print('Response was: {:s}\n'.format(response))
        try:
            switch_dict.get(response)()
        except TypeError:
            print('Not a valid response. Type 1, 2, 3, or 4\n')
        continue


if __name__ == '__main__':
    mainloop()
