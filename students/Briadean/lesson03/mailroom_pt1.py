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
# donors_viewobj = donors.items()  # this returns tuple, which i want because tuples are sortable?
#
# for x in donors_viewobj:
#     print(x)


def menu():
    main_menu = ("Welcome to The Mailroom!\n\n"
                 "Please choose from the following options:\n"
                 "1: Send a Thank You\n"
                 "2: Create a Report\n"
                 "3: Quit\n")

    valid_response = ["1", "2", "3"]
    print(main_menu)
    response = input(">> ").title()

    while response not in valid_response:
        response = input("{} is not an available option. Please enter 1, 2 or 3.\n"
                         ">> ".format(response))

    while response in valid_response:
        if response == "1":
            thank_you()
        elif response == "2":
            create_report()
        elif response == "3":
            exit_()


def thank_you():
    thankyou_menu = ("You selected Send a Thank You!\n\n"
                     "Please enter the full name of the donor you would like to thank below.\n"
                     "Type 'List' to view previous donors to select from.\n"
                     "Type 'Quit' to exit to the main menu.\n")

    thankyou_template = ("\n\nDear {},\n\n"
                         "Thank you for your generous {} donation which will allow us to continue\n"
                         "our fight against the tyranny of the flying spaghetti monster and help\n"
                         "rebuild the devastation caused by his meatballs.\n\n"
                         "All donations received by our organization go directly to fund R&D geared\n"
                         "towards stopping this vicious beast, rebuilding of areas devastated by meatballs\n"
                         "and paying our meatball eaters a fair and livable wage.\n\n"
                         "Many Thanks,\n"
                         "Team Meatball Eaters\n\n")

    valid_response = ["List", "Quit"]
    print(thankyou_menu)
    response = input(">> ").title()
    donor_names = donors.keys()

    if response not in valid_response:
        donors.setdefault(response, [])
        print(donor_names)  # Delete this check after it works correctly!
        donation_amt = input(int("How much are they donating today? >> $ "))
        donors[response].append(donation_amt)
        print(thankyou_template.format(response, donation_amt))

    for response in valid_response:
        if response == "List":
            print(donor_names)  # Currently this return "dict_keys([names])" make pretty!
            response = input(">> ").title()  # This isn't evaluating right now. fix! Maybe turn if above into function?
        elif response == "Quit":
             menu()  # This may deepen the stack. Another way to get back to main menu function?


def create_report():
    report_header = ("Donor Name          | Total Given | Num Gifts | Average Gift\n"
                     "------------------------------------------------------------\n")
    report_line = "{:20} ${:12,.2f}{:11} ${:12}".format("banana", 400, 6, 60)  #
    # I thought d would make it so many from left, linter complaining?


    print(report_header, report_line)


def exit_():
    response = input("Are you sure you'd like to exit the program? Y/N\n >> ").capitalize()
    valid_response = ["Y", "N"]
    while response in valid_response:
        if response == "N":
            menu()
        elif response == "Y":
            sys.exit()
        else:
            response = input("{} is not an available option. Please enter Y or N\n >> ".format(response))


thank_you()
