#!/usr/bin/env python

"""

Mailroom program for a non profit

"""

import sys

donor_db = [("Britney Spears", [50.99, 100.99, 2000.99]),
            ("Christina Aguilera", [50.99, 100.99, 2000.99]),
            ("Mandy Moore", [50.99, 100.99, 2000.99]),
            ("Jessica Simpson", [50.99, 100.99, 2000.99]),
            ("Queen Bey", [50.99, 100.99, 2000.99]),
            ]

def mainloop():
    print("Welcome to the Mailroom \n")
    main_menu()


def main_menu():
    print("Main Menu:")
    print(
      "T - Send a thank you\n"
      "R - Create a report\n"
      "Q - Quit the program"
      )
    menu_selection = input("\nChoose a letter:  ")
    menu_selection = menu_selection.upper().strip()
    while True:
        if menu_selection == "T":
            thank_you()
        elif menu_selection == "R":
            create_report()
        elif menu_selection == "Q":
            quit_program()
        else:
            print("Invalid response -- select T, R, or Q \n")

def thank_you():
    print("\nMenu: Send a Thank You\n")
    while True:
        donor_name = input("Enter the donor's full name. \nEnter 'list' to see a list of donors, \n or 'menu' to return to the main menu: ").strip()
        if donor_name.lower() == "list":
            print("\nDonor database:")
            for donor in donor_db:
                print(donor[0])
            print("\n")
        elif donor_name.lower() == "menu":
            return main_menu()
        else:
            break

    while True:
        donor_amount = input("Enter amount of donation amount (or 'menu' to exit): ").strip()
        if donor_amount.lower() == "menu":
            return
        else:
            break
    #I borrowed this from the example solution. Could you please explain None to me? 
    donor = find_donor(donor_name)
    if donor is None:
        donor = (donor_name, [])
        donor_db.append(donor)

    donor[1].append(float(donor_amount))
    
    print(ty_letter(donor_name, donor_amount))


def find_donor(donor_name):
    for donor in donor_db:
        if donor_name.strip().lower() == donor[0].lower():
            return donor
    return None


def ty_letter(donor_name, donor_amount):
    print("\nMenu: Send a Thank You, Letter\n")
    #How can I input the donation amount?? Why does donor_amount not work here?
    print(f"\nDear {donor_name.title()},\n\n\tYour donation of ${donor_amount} will make a great difference to a young learner at the coding academy. Thank you.\n\n\nSincerely,\nAn Academy Student\n")
    #{donor_amount:,.2f}
    print("---------------------")


def create_report():
    report_rows = []
    for (name, donations) in donor_db:
        total_donations = sum(donations)
        num_donations = len(donations)
        avg_donations = total_donations / num_donations
        report_rows.append((name, total_donations, num_donations, avg_donations))

    print("\nMenu: Create a Report\n")
    header_titles = ("Donor Name ","Total Given ", "Num Gifts ","Average Gift ")
    header = "{:20}| {:10}| {:10}| {:10}".format(*header_titles)
    print(header)
    print("-" * 61)
    for row in report_rows:
    #need to correct my formatting of the $ symbol
        print("{:20s} ${:2.2f} {:5d} ${:14.2f}".format(*row))
    print("-"*61)
    print("\n")
    return main_menu()
 

def quit_program():
    print("You have exited the Mailroom.")
    sys.exit()


if __name__ == "__main__":
    mainloop()

