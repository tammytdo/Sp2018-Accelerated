#!/usr/bin/env python

import sys
# It should have a data structure that holds a list of your donors and a history of the amounts they have donated. This structure should be populated at first with at least five donors, with between 1 and 3 donations each.
#
# You can store that data structure in the global namespace.
#
# The script should prompt the user (you) to choose from a menu of 3 actions: “Send a Thank You”, “Create a Report” or “quit”)
#
# Sending a Thank You
# If the user (you) selects ‘Send a Thank You’, prompt for a Full Name.
# If the user types ‘list’, show them a list of the donor names and re-prompt
# If the user types a name not in the list, add that name to the data structure and use it.
# If the user types a name in the list, use it.
# Once a name has been selected, prompt for a donation amount.
# Turn the amount into a number – it is OK at this point for the program to crash if someone types a bogus amount.
# Once an amount has been given, add that amount to the donation history of the selected user.
# Finally, use string formatting to compose an email thanking the donor for their generous donation. Print the email to the terminal and return to the original prompt.
# It is fine (for now) to forget new donors once the script quits running.
#
# Creating a Report
# If the user (you) selected “Create a Report”, print a list of your donors, sorted by total historical donation amount.
# Include Donor Name, total donated, number of donations and average donation amount as values in each row. You do not need to print out all their donations, just the summary info.
# Using string formatting, format the output rows as nicely as possible. The end result should be tabular (values in each column should align with those above and below)
# After printing this report, return to the original prompt.
# At any point, the user should be able to quit their current task and return to the original prompt.
# From the original prompt, the user should be able to quit the script cleanly.
# Your report should look something like this:
#
# Donor Name                | Total Given | Num Gifts | Average Gift
# ------------------------------------------------------------------
# William Gates, III         $  653784.49           2  $   326892.24
# Mark Zuckerberg            $   16396.10           3  $     5465.37
# Jeff Bezos                 $     877.33           1  $      877.33
# Paul Allen                 $     708.42           3  $      236.14

donors = {"Bee": [100, 25, 75], "Puppycat": [10, 200], "Deckard": [15, 15, 15, 15, 15]}

def menu():
    message = ("Welcome to The Mailroom!\n\n"
               "Please choose from the following options:\n"
               "1 Send a Thank You\n"
               "2 Create a Report\n"
               "3 Quit\n")

    print(message)
    response = None
    valid_response = ["1","2","3"]

    while response in valid_response:
        response = input(">> ")
        if response == "1":
            thank_you()
        elif response == "2":
            create_report()
        elif response == "3":
            exit_()
        else:
            response = input ("{} is not an available option. Please enter 1, 2 or 3.".format(response))


def thank_you():
    print("You selected Send a Thank You!\n")


def create_report():
    print("You selected Create a Report!\n")


def exit_():
    response = input("Are you sure you'd like to exit the program? Y/N\n >> ")
    valid_response = ["Y", "y", "N", "n"]
    while response in valid_response:
        if response == "N" or "n":
            menu()
        elif response == "Y" or "y":
            sys.exit()
        else:
            response = input("{} is not an available option. Please enter Y or N\n >> ".format(response))


menu()
