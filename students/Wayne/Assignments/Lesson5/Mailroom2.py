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




def list_donors():
    print("Donors:\n")
    for donor in donors:
        print(donor[0])


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

# Builds the quit function to exit the application


def quit():
    sys.exit()


def mainloop():

    mainmenuinput = input(dedent("""
        What would you like to do?

        (1) - Send a Thank You Letter
        (2) - Build a Report
        (3) - Quit

        > """))
    return mainmenuinput.strip()


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
