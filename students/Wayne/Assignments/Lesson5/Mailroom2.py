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

        print(thankyou)

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
        (3) - Quit

        > """))
    return mainmenuinput.strip()


def thankyou():
    while True:
        name = input("Enter the donor's name or a list of donor's"
                     "names to see all donors (or type 'menu'"
                     "to exit)>").strip()
        if name == 'list':
            print(list_donors())
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
        letter = thankyou(donor)
        filename = donor[0].replace(" ", "_") + ".txt"
        print("creating letter to:", donor[0])
        open(filename, 'w').write(letter)

# ----------------------------------------------------------------------------
#
# Prints the donor report
#
# ----------------------------------------------------------------------------


def print_donor_report():
    print(donor_report)


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

    mainlist_dict = {"1": thankyou,
                     "2": print_donor_report,
                     "3": save_letters_to_disk,
                     "4": quit}



    running = True
    while running:
        response = mainloop()
        if response not in ('1', '2', '3'):
            print("Not a Valid Response, input 1, 2, or 3")
            continue
        elif response == '1':
            thankyou()
        elif response == '2':
            donor_report()
        elif response == '3':
            quit()
