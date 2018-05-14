#!/usr/bin/env python3

"""
OO mailroom program
"""

from donor_class import Donor
from donor_class import DonorDB

import sys, os
# donors = {"William Gates, III": [10000, 2000000, 5000, 550000],
#           "Mark Zuckerberg": [10, 100, 25, 100],
#           "Jeff Bezos": [50,  10, 15, 100],
#         }

def my_args(mydonorDB, arg_dict, response):
    try:
        myresponse = int(response)
    except ValueError:
        print("ValueError: Invalid Response")
        return
    try:
        result = arg_dict[myresponse]
    except KeyError:
        print("KeyErorr: Invalid Response")
        return

    result(mydonorDB)


def quit(response):
    if response == "1":
        print("You have chosen to exit Mailroom! GoodBye!")
        sys.exit()
    else:
        return "Returning to Mailroom"

def to_quit():
    print(menu_string("quit"))
    response=get_input()
    print(quit(response))

def get_input():
    return input(">>")

def thank_you_loop(mydonorDB):
    while True:
        print(menu_string("thank_you"))
        response = get_input()
        if response == "3":
            print("\nReturning to main menu:\n")
            break
        elif response == "4":
            to_quit()
        else:
            add_donor_dict = {1: add_donation,
                          2: list_donors}
            my_args(mydonorDB, add_donor_dict, response)

def add_donation(mydonorDB):
    print("Enter Donor Name")
    name = get_input()
    print("Enter donation amount")
    donation = get_input()

    d = Donor(name, int(donation))
    mydonorDB.update_donor(d)

def list_donors(mydonorDB):
    print("\nHere is a list of current Donors:")
    print("\n".join(mydonorDB.list_donors))

def print_report(mydonorDB):
    print("\n".join(mydonorDB.generate_printable_report()))


def report(mydonorDB):
    print("Donor Name                | Total Given | Num Gifts | Average Gift")
    print("-"*66)
    print_report(mydonorDB)

def send_letters(mydonorDB):
    for donor, donations in donors.items():
        filename = donor.replace(" ", "_") + ".txt"
        with open(filename, "w") as infile:
            infile.write("Dear {},\n\n".format(donor))
            infile.write("\tThank you for your generous donation of {}\n\n".format(donations[-1]))
            infile.write("\tIt will be put to very good use.\n\n")
            infile.write("\t\t\t\t\t   Sincerely, \n\t\t\t\t\t   The Team\n")


def welcome_message():
    return "Welcome to Mailroom!"

def menu_string(input):
    menu_string = {"main" : """\
        \nPlease select from the following options:\
        \n1. Create a Donation\
        \n2. Create a Donor Report\
        \n3. Send thank you letters to everyone\
        \n4. Exit Program""",
    "thank_you": """\
        \nPlease select from the following options:\
        \n1. Add a new donor\
        \n2. List donors\
        \n3. Quit to main menu\
        \n4. Exit Program\
        """,
    "quit": """All your unsaved changes will be lost. Are you sure you want to exit?\
        \n1. Exit\
        \n2. Return to Mailroom"""}
    return menu_string[input]

def mainloop():
    print(welcome_message())
    #Create empty Donor Database
    mydonorDB = DonorDB()
    while True:
        print(menu_string("main"))
        response = get_input()
        print("Your response was: {}".format(response))

        menu_dict = {1: thank_you_loop, 2: report,
                     3: send_letters}

        if response == "4":
            to_quit()
        else:
            my_args(mydonorDB, menu_dict, response)

        ### added try/except clause

if __name__ == "__main__":
    mainloop()
