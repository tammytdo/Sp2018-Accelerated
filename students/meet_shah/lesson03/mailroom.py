#!/usr/bin/env python3

"""
simple mailroom program for a non-profit
"""

import sys

donors = {"William Gates, III": [10000, 2000000, 5000, 550000],
          "Mark Zuckerberg": [10, 100, 25, 100],
          "Jeff Bezos": [50,  10, 15, 100],
        }

def thank_you():
    while True:
        new_response = input("Enter a command. Your options are [list, <donor name>, q(quit),]>>")
        if new_response == "list":
            for donor in donors:
                print(donor[0])
        elif response in ['q','quit']:
            print("Returning to the main menu")
            break
            sys.exit()


def print_report(t):
    return '{:20}{:>15}{:>16}{:>15}'.format(*t)


def report():
    print("Donor Name                | Total Given | Num Gifts | Average Gift")
    print("-"*66)
    for donor, donations in donors.items():
        total_donations = sum(donations)
        num_donations = len(donations)
        average_donations = total_donations * 1.0 / num_donations
        print(print_report((donor, total_donations, num_donations, average_donations)))




def quit():
    print("You have chosen to quit! GoodBye!")
    sys.exit()

def mainloop():
    print("Welcome to Mailroom")
    response = ""
    while True:
        print("What do you want to do? Choose from a menu of 3 actions:")
        print("1. Send a Thank You")
        print("2. Create a Report")
        print("3. Quit")
        response = input(">>")
        print("Your response was:", response)

        if response not in ("1", "2", "3"):
            print("***Not a Valid response. Please choose from the listed options***\n")
            continue

        if response == "1":
            thank_you()
        elif response == "2":
            report()
        elif(response == "3"):
            quit()


if __name__ == "__main__":
    mainloop()
