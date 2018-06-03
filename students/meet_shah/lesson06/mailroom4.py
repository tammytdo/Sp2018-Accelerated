#!/usr/bin/env python3

"""
simple mailroom program for a non-profit
"""

import sys

def quit(mydonorDB):
    print("You have chosen to quit! GoodBye!")
    sys.exit()


def menu_generator(menu_option):
        menu_dict = {"main": """
What do you want to do? Please choose from below options:
1. Send a thank you
2. Create a report
3. Send letters to everyone
4. Quit
    """,
    "thank_you": """
Please choose from the below options
1. List Donors
2. Send a thank you
3. Return to the main menu
    """}
        return menu_dict[menu_option]

def args(mydonorDB, arg_dict, response):
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

    print(result(mydonorDB))


def get_input():
    response = input(">>")
    print("Your response was:", response)
    return response


def list_donors(mydonorDB):
    print("\nHere's a list of our donors:\n")
    ### Added list comprehension ###
    return "\n".join([(donor) for donor, _ in mydonorDB.items()])

def add_donor(mydonorDB):
    print("Enter donor name")
    donor_name = get_input()
    print("Enter the donation amount")
    donation = get_input()
    try:
        donation = int(donation)
    except ValueError:
        return "Value error. Please enter a number donation amount"

    mydonorDB.setdefault(donor_name, []).append(donation)
    return "Dear {}, We gladly accept your generous donation of ${}".format(donor_name,donation)


def thank_you(mydonorDB):
    while True:
        print(menu_generator("thank_you"))
        response = get_input()

        thank_you_dict = {1: list_donors, 2: add_donor}
        if response == "3":
            # return empty string to break out of the loop
            return ""

        args(mydonorDB, thank_you_dict, response)


def generate_report(t):
    return '{:20}{:>20}{:>12}{:>14}'.format(*t)


def report(mydonorDB):
    print("Donor Name                | Total Given | Num Gifts | Average Gift")
    print("-"*66)
    reverse_donor = {}
    for donor, donations in mydonorDB.items():
        total_donations = sum(donations)
        reverse_donor[total_donations] = donor

    total_donations = sorted(reverse_donor.keys(), reverse=True)
    for total_donation in total_donations:
        donor = reverse_donor[total_donation]
        num_donations = donors[donor]
        num_donations = len(donations)
        average_donations = total_donation * 1.0 / num_donations
        average_donations = "${:,.2f}".format(average_donations)
        total_donation = "${:,.2f}".format(total_donation)
        print(generate_report((donor, total_donation, num_donations, average_donations)))

def send_letters(mydonorDB):
    for donor, donations in mydonorDB.items():
        filename = donor.replace(" ", "_") + ".txt"
        thank_you_letter = generate_donor_letter(dnoor, donations[-1])
        with open(filename, "w") as infile:
            infile.write(thank_you_letter)

def generate_donor_letter(donor, donation):
    donor_string = "Dear {},\n\n".format(donor) + \
    "\tThank you for your generous donation of {}\n\n".format(donation) + \
    "\tIt will be put to very good use.\n\n" + \
    "\t\t\t\t\t   Sincerely, \n\t\t\t\t\t   The Team\n"
    return donor_string

def welcome_message():
    return "Welcome to Mailroom"

def mainloop():
    print(welcome_message())

    mydonorDB = {"Bill Gates": [10000, 2000000, 5000, 550000],
              "Mark Zuckerberg": [10, 100, 25, 100],
              "Jeff Bezos": [50,  10, 15, 100]
              }

    while True:

        menu_dict = {1: thank_you, 2: report,
                     3: send_letters, 4: quit}

        print(menu_generator("main"))
        response = get_input()
        args(mydonorDB, menu_dict, response)


if __name__ == "__main__":
    mainloop()
