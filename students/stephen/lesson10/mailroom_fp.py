#!/usr/bin/env python

"""
Simple Mailroom Program for a nonprofit
"""

# The script should prompt the user (you) to choose from a menu of 3 actions:
# “Send a Thank You”, “Create a Report” or “quit”)

import os, sys
import json

# Create a data object to store donor information
# donors = {
#     'Jeff Bezos': [50, 100, 56],
#     'Mark Zuckerberg': [45, 105, 349, 101, 78],
#     'Paul Allen': [10, 50, 400, 400],
#     'Elon Musk': [16, 68, 170, 425],
#     'Richard Branson': [25, 90, 124, 300]
# }

class Donor:
    """
    Handles the donor
    """
    def __init__(self, name, *donations):
        self._name = name
        self._donations = list(donations)

    @property
    def name(self):
        return self._name

    @property
    def donations(self):
        return self._donations

    @donations.setter
    def donations(self, lst):
        self._donations = lst

    def add_donation(self, donation):
        self._donations.append(donation)

    @property
    def total_donations(self):
        return sum(self._donations)
        # return reduce(lambda a, x: a+x, self._donations, 0)
        # s = 0
        # for d in donations:
        #     s += d
        # return s

    @property
    def count_donations(self):
        return len(self._donations)

    @property
    def average_donation(self):
        return self.total_donations / self.count_donations

    @property
    def letter(self):
        """
        Takes the donor iterable and returns a string that is a formatted thank you note
        with the donor's name and last donation amount.
        """
        return "Dear {:s},\n\nWe greatly appreciate your generous donation of ${:,.2f}.\n\nThank you,\nThe Team".format(self._name, self._donations[-1])

    @property
    def filename(self):
        'Return a txt file name based on the donor name and using underscores instead of spaces'
        return self._name.replace(' ', '_') + '.txt'

    # allow other items to call the class
    def __repr__(self):
        return "{}: {}".format(self._name, self._donations)  

class DonorDB:
    """
    Handles collection of donors
    """
    def __init__(self):
        self._donors = {}

    def add_donor(self, donor):
        if donor.name.lower() in self._donors:
            self._donors[donor.name.lower()].add_donation(*(donor.donations))
        else:
            self._donors[donor.name.lower()] = donor

    def get_total_from_donor(self, donor_name):
        return self._donors[donor_name.lower()].total_donations

    def get_donor(self, donor_name):
        try:
            return self._donors[donor_name.lower()]
        except KeyError:
            print('Donor does not exist in the database')

    @property
    def export(self):
        return {donor.name:donor.donations for donor in self._donors.values()}

    def donor_list(self):
        name_list = [donor.name for donor in self._donors.values()]
        return '\n'.join(name_list)

    def letters_to_disk(self):
        """
        Generate one letter for each donor and write to disk
        """
        for donor in self._donors.values():
            print('Generating letter to {:s}'.format(donor.name))
            with open(donor.filename, 'w') as outfile:
                outfile.write(donor.letter)
        print()

    def report(self):
        sorted_donors = [donor for donor in self._donors.values()]
        sorted_donors.sort(key=lambda donor: donor.total_donations, reverse=True)
        report_rows = []
        for d in sorted_donors:
            report_rows.append('{:26s} {:>12s} {:^13d} {:>12s}'.format(d.name, '${:,.2f}'.format(d.total_donations), d.count_donations, '${:,.2f}'.format(d.average_donation)))
        header = ('Donor Name                | Total Given | Num Gifts | Average Gift\n') + ('-' * 66) + '\n'
        return header + '\n'.join(report_rows) + '\n'

    @property
    def count_donors(self):
        return len(self._donors)

    @property
    def count_donations(self):
        return sum([len(donor.donations) for donor in self._donors.values()])

    @property
    def total_donations(self):
        return sum([donor.total_donations for donor in self._donors.values()])

    @property
    def average_total_donation(self):
        return self.total_donations / self.count_donors

    @property
    def average_single_donation(self):
        return self.total_donations / self.count_donations

    def __repr__(self):
        return str([d for d in self._donors.values()])

    @property
    def projection(self):
        return {d[0]:d[1] for d in self._projection}

    def challenge(self, x=1, mn=0, mx=float("inf")):
        self._projection = []
        for k, v in self.export.items():
            self._projection.append((k, list(map(lambda y: y * x, list(filter(lambda z: z >= mn and z <= mx, v))))))
        self._projection.sort(key=lambda z: sum(z[1]), reverse=True)
        # self.projection = {d[0]:d[1] for d in self._projection}

    def projection_report(self):
        report_rows = []
        for d in self._projection:
            report_rows.append('{:26s} {:>12s} {:^13d} {:>12s}'.format(d[0], '${:,.2f}'.format(sum(d[1])), len(d[1]), '${:,.2f}'.format(sum(d[1]) / len(d[1]))))
        header = ('Donor Name                | Total Given | Num Gifts | Average Gift\n') + ('-' * 66) + '\n'
        return header + '\n'.join(report_rows) + '\n'


class Menu:
    response = None

    def __init__(self, title, menu):
        self._title = title
        self._menu = menu
        error_msg = 'Not a valid response. Enter '
        for key in self._menu:
            error_msg += key + ', '
        self._error = error_msg[:-3] + 'or ' +  error_msg[-3] + '.\n'

    def menu(self):
        m = [str(k) + ') ' + str(v[0]) + '\n' for k, v in self._menu.items()]
        return ''.join(m)

    def get_response(self):
        print(self._title)
        print(self.menu())
        response = input('>> ')
        while response not in self._menu:
            print(self._error)
            response = input('>> ')
        self.response = response

    @property
    def switch(self):
        return {k:v[1] for k, v in self._menu.items()}


def print_projection():
    print('\nProject totals for a donation challenge:\n\nEnter a donation multiplying factor')
    multiplier = input('>> ')
    ex = 0
    while ex == 0:
        try:
            multiplier = float(multiplier)
        except ValueError:
            print('Please enter a valid multiplier')
            multiplier = input('>> ')
            continue
        else:
            ex = 1
    print('Enter the minimum donation to consider (0 for no minimum)')
    mn = input('>> ')
    ex = 0
    while ex == 0:
        try:
            mn = float(mn)
        except ValueError:
            print('Please enter a valid minimum')
            mn = input('>> ')
            continue
        else:
            ex = 1
    print('Enter the maximum donation to consider (leave blank for no maximum)')
    mx = input('>> ')
    while (mx != '') and (type(mx) not in [int, float]):
        print('Please enter a valid maximum')
        mx = input('>> ')
    if mx == '':
        mx = float("inf")
    donor_db.challenge(multiplier, mn, mx)
    print('\nProjected report based on past donations:')
    print(donor_db.projection_report())
    return

def print_report():
    print(donor_db.report())

def return_to_main():
    return

def write_letters_to_disk():
    """
    Generate one letter for each donor and write to disk
    """
    donor_db.letters_to_disk()
    return

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
    d = Donor(name, amount)
    donor_db.add_donor(d)
    print(d.letter)
    print()

def get_name_donation():
    print('\nEnter the full name of the donor')
    ty_name = input('>> ')
    print('Enter a donation amount')
    ty_amount = input('>> ')
    print()
    enter_name(ty_name, ty_amount)
    return

def print_donor_list():
    print('\nDonors:')
    print(donor_db.donor_list(), '\n')
    pass

def thank_you():
    ty = Menu('Thank You Menu:', thank_you_menu)
    ty.get_response()
    ty.switch.get(ty.response)()
    return

def quit_program():
    """
    Save donor list to json file
    """
    export_db = donor_db.export
    with open('donor_db.json', 'w') as fp:
        json.dump(export_db, fp, sort_keys=True, indent=4)
    
    sys.exit()

main_menu = {
    '1': ['Send a Thank You', thank_you]
    , '2': ['Create a Report', print_report]
    , '3': ['Create a Projected Report', print_projection]
    , '4': ['Send letters to everyone', write_letters_to_disk]
    , '5': ['Quit', quit_program]
    }

thank_you_menu = {
    '1': ['Enter a donor', get_name_donation]
    , '2': ['See a list of donor names', print_donor_list]
    , '3': ['Return to the Main Menu', return_to_main]
    }

def mainloop():
    print('Welcome to Mailroom\n')
    main = Menu('Main Menu:', main_menu)
    while True:
        main.get_response()
        main.switch.get(main.response)()

if __name__ == '__main__':
    # Load existing database
    with open('donor_db.json', 'r') as fp:
        db = json.load(fp)
    # Load DonorDB object
    donor_db = DonorDB()
    for n, d in db.items():
        donor = Donor(n, *d)
        donor_db.add_donor(donor)
    mainloop()
