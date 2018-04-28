"""
Simple mailroom program for a non profit
"""

# Start with interactive loop

import sys
import math

from textwrap import dedent


# ----------------------------------------------------------------------------
#
# Built a sample database and put it into a dict format
#
# ----------------------------------------------------------------------------


def find_donor_db():
    return{'dave grohl': ("Dave Grohl", [999,999.99, 45.63]),
           'billy joe armstrong': ("Billy Joe Armstrong", [15,000, 2,222]),
           'rivers cuomo': ("Rivers Cuomo", [1994.96, 2,100,000]),
           }

# ----------------------------------------------------------------------------
#
# The following function adds a new donor to the db. The function below uses
# .lower() to convert all of the donor names into a single case to allow for
# an easier sorting method of the dict.
#
# ----------------------------------------------------------------------------


def add_new_donor(name):
    name = name.strip()
    donor = (name, [])
    donor_db[name.lower()] = donor
    return donor

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
# The following function creates a sort key for the donor db. Allows the user
# to sort by name.
#
# ----------------------------------------------------------------------------


def sort_key(item):
    return item[1]


# ----------------------------------------------------------------------------
#
# The following function creates a sort key for the donor db. Allows the user
# to sort by name.
#
# ----------------------------------------------------------------------------


def thankyou():
    while True:
        name = input("Enter the donor's name or a list of donor's"
                     "names to see all donors (or type 'menu'"
                     "to exit)>").strip()
        if name == 'list':
            list_donors()
        elif name == 'menu':
            return
        else:
            break

# creates loop for donation amount input

    while True:
        donationinput = input("Enter the amount donated "
                              "(or 'menu' to exit)>").strip()
        if donationinput == 'menu':
            return

# Building reporting function


def report():
    print("This is the report function\n")


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
        (3) - Quit

        > """))
    return mainmenuinput.strip()


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

    running = True
    while running:
        response = mainloop()
        if response not in ('1', '2', '3'):
            print("Not a Valid Response, input 1, 2, or 3")
            continue
        elif response == '1':
            thankyou()
        elif response == '2':
            report()
        elif response == '3':
            quit()
