"""
Simple mailroom program for a non profit
"""

# Start with interactive loop

import sys
import math

from textwrap import dedent


"""
The following section of code pertain to the building and manipulation of the
donors database.
"""

# ----------------------------------------------------------------------------
#
# Built a sample database and put it into a dict format
#
# ----------------------------------------------------------------------------


def find_donor_db():
    return{'dave grohl': ("Dave Grohl", [999999.99, 45.63]),
           'billy joe armstrong': ("Billy Joe Armstrong", [15000, 2222]),
           'rivers cuomo': ("Rivers Cuomo", [1994.96, 2100000]),
           }


# def object_oriented_db():
#     db = find_donor_db()
#     raw_data = find_donor_db()

#     for k, v in raw_data.items():
#         donor = Donor(k)
#         for donation in v:
#             donor.add_donation(donation)

# ----------------------------------------------------------------------------
#
# Building donor class that handles all items pertaining to storing a donor
#
# ----------------------------------------------------------------------------


class Donor:
    def __init__(self, name, donations=None):
        self.name = name
        self.donations = [] if donations is None else donations

        @property
        def name(self):
            return self.name

        @property
        def donations(self):
            return self.donations

        def add_donation(self, donation):
            return self.donations.append(donation)

        @property
        def total_donations(self):
            return sum(self.donations)

# ----------------------------------------------------------------------------
#
# Building db class that handles all items pertaining to adding and storing
# donor information
#
# ----------------------------------------------------------------------------


class DonorData:
    def __init__(self, donors =None):
        self.donors = {}
        self.donations = {} if donations is None else {d.}


    def add_donor(self, donor):
        self.donors[donor.name.lower()] = donor

    def get_total_from_donor(self, donor_name):
        return self.donors[donor_name.lower()] = donor

    @property
    def list_donors():
    listing = ("Donors:")
    for donor in self.donor_db.values():
        listing.append(donor[0])
    return "\n".join(listing)

    def search_donor_db(name):
    key = self.name.strip().lower()
    return donor_db.get(key)


# ----------------------------------------------------------------------------
#
# The following function adds a new donor to the db. The function below uses
# .lower() to convert all of the donor names into a single case to allow for
# an easier sorting method of the dict.
#
# ----------------------------------------------------------------------------

# **************************** Moved to donor class **************************

# def add_new_donor(name):
#     name = name.strip()
#     donor = (name, [])
#     donor_db[name.lower()] = donor
#     return donor

# ----------------------------------------------------------------------------
#
# The following function uses the dictionary key to search the donor database
#
# ----------------------------------------------------------------------------


def search_donor_db(name):
    key = name.strip().lower()
    return donor_db.get(key)

# ----------------------------------------------------------------------------
#
# The following function creates a list of donors from the database
#
# ----------------------------------------------------------------------------


def list_donors():
    listing = ("Donors:")
    for donor in donor_db.values():
        listing.append(donor[0])
    return "\n".join(listing)


# ----------------------------------------------------------------------------
#
# The following function adds a new donation amount into the database
#
# ----------------------------------------------------------------------------


def accept_donation(name):
    while True:
        donation_msg = input("Enter your desired donation amount"
                             "or 'menu' to exit)>").strip()
        if donation_msg == "menu":
            return
        else:
            donation_amt = float(donation_msg)
            break

    donor = search_donor_db(name)
    if donor is None:
        donor = add_new_donor(name)

        donor[1].append(donation_amt)

        print(thank_you_message())

# ----------------------------------------------------------------------------
#
# The following function creates a sort key for the donor db. Allows the user
# to sort by name.
#
# ----------------------------------------------------------------------------


def sort_key(item):
    return item[1]


"""
The following section of the code pertaions to the operational side of the
mail room application.
"""

# ----------------------------------------------------------------------------
#
# Mainloop
#
# ----------------------------------------------------------------------------


def mainloop():

    mainmenuinput = input(dedent("""
        What would you like to do?

        (1) - Send a Thank You Letter
        (2) - Build a Report
        (3) - Send letters to all donors
        (4) - Quit

        > """))
    return mainmenuinput.strip()


def thank_you_message():
    while True:
        name = input("Enter the donor's name or a list of donor's"
                     "names to see all donors (or type 'menu'"
                     "to exit)>").strip()
        if name == 'list':
            print(list_donors())
        elif name == 'menu':
            return
        else:
            accept_donation(name)

# creates loop for donation amount input

    while True:
        donationinput = input("Enter the amount donated "
                              "(or 'menu' to exit)>").strip()
        if donationinput == 'menu':
            return

# ----------------------------------------------------------------------------
#
# Makes a standardized letter template that passes through the donor name and
# and the amount donated
#
# ----------------------------------------------------------------------------

def write_letter(donor):

    return dedent('''Dear {0:s},

        Thank you for your kind doation of ${1:.2f}.
        We will make sure that it is put to very good use.

                                    Sincerely,
                                        - The American Cancer Society)
        '''.format(donor[0], donor[1][-1]))

# ----------------------------------------------------------------------------
#
# Builds the donor report and displays the name, total given, number of gifts
# and the average gift donated by the donor.
#
# ----------------------------------------------------------------------------


def donor_report():

    report_rows = []
    for (name, donation_amt) in donor_db.values():
        total_donations = sum(donation_amt)
        num_donations = len(donation_amt)
        avg_donation = total_donations / num_donations
        report_rows.append((name, total_donations, num_donations, avg_donation))

    report_rows.sort(key=sort_key)
    report = []
    report.append("{:25s} | {:11s} | {:9s} | {:12s}".format("Donor Name",
                                                            "Total Donated",
                                                            "Num gifts",
                                                            "Average Donation"))
    report.append("_" * 66)
    for row in report_rows:
        report.append("{:25s}   ${:10.2f}   ${:9d}   ${:11.2f}".format(*row))
    return "\n".join(report)

# ----------------------------------------------------------------------------
#
# Save letters to disk
#
# ----------------------------------------------------------------------------


def save_letters_to_disk():
    for donor in donor_db.values():
        letter = write_letter(donor)
        filename = donor[0].replace(" ", "_") + ".txt"
        print("creating letter to:", donor[0])
        open(filename, 'w').write(letter)

# ----------------------------------------------------------------------------
#
# Prints the donor report
#
# ----------------------------------------------------------------------------


def print_donor_report():
    print(donor_report())


# ----------------------------------------------------------------------------
#
# quits the program when prompted in the menu
#
# ----------------------------------------------------------------------------


def quit():
    sys.exit()

# ----------------------------------------------------------------------------
#
# Creates the main function for the Mailroom2.py exercise
#
# ----------------------------------------------------------------------------


if __name__ == "__main__":

    donor_db = find_donor_db()

    mainlist_dict = {"1": thank_you_message,
                     "2": print_donor_report,
                     "3": save_letters_to_disk,
                     "4": quit}

    while True:
        action = mainloop()
        try:
            mainlist_dict[action]()
        except KeyError:
            print("error: menu selection is invalid!")
