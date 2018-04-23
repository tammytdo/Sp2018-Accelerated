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
            for donor, _ in donors.items():
                print(donor)
        elif new_response in ['q','quit']:
            print("Returning to the main menu")
            break
        else:
            donor = new_response
            donation = input("Enter the amount you would like to donate: ")
            donation = int(donation)
            donors.setdefault(new_response, []).append(donation)
            print("Dear {}, We gladly accept your generous donation of ${}".format(donor,donation))
            print("Please visit us anytime to add more donations")
            break




def print_report(t):
    return '{:20}{:>15}{:>16}{:>15}'.format(*t)


def report():
    print("Donor Name                | Total Given | Num Gifts | Average Gift")
    print("-"*66)
    reverse_donor = {}
    for donor, donations in donors.items():
        total_donations = sum(donations)
        reverse_donor[total_donations] = donor

    total_donations = sorted(reverse_donor.keys(), reverse=True)
    for total_donation in total_donations:
        donor = reverse_donor[total_donation]
        num_donations = donors[donor]
        num_donations = len(donations)
        average_donations = total_donation * 1.0 / num_donations
        print(print_report((donor, total_donation, num_donations, average_donations)))

def send_letters():
    for donor, donations in donors.items():
        filename = donor.replace(" ", "_") + ".txt"
        with open(filename, "w") as infile:
            infile.write("Dear {},\n\n".format(donor))
            infile.write("\tThank you for your generous donation of {}\n\n".format(sum(donations)))
            infile.write("\tIt will be put to very good use.\n\n")
            infile.write("\t\t\t\t\t   Sincerely, \n\t\t\t\t\t   The Team\n")




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
        print("3. Send letters to everyone")
        print("4. Quit")
        response = input(">>")
        print("Your response was:", response)

        if response not in ("1", "2", "3", "4"):
            print("***Not a Valid response. Please choose from the listed options***\n")
            continue

        if response == "1":
            thank_you()
        elif response == "2":
            report()
        elif response == "3":
            send_letters()
        elif(response == "4"):
            quit()


if __name__ == "__main__":
    mainloop()
