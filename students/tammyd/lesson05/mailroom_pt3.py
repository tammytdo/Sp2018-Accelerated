#!/usr/bin/env python

"""

Mailroom program for a non profit

"""

import sys

donor_db = {"britney spears": ("Britney Spears", [50.99, 100.99, 1000.99]),
            "christina aguilera": ("Christina Aguilera", [50.99, 100.99, 2000.99]),
            "mandy moore": ("Mandy Moore", [50.99, 100.99, 3000.99]),
            "jessica simpson": ("Jessica Simpson", [50.99, 100.99, 4000.99]),
            "queen bey": ("Queen Bey", [50.99, 100.99, 5000.99]),
            }

def donor_database():
    return donor_db


def mainloop():
    print("Welcome to the Mailroom \n")
    main_menu()


def main_menu():
    print("Main Menu:")
    print(
      "T - Send a Thank You\n"
      "L - Send a Letter to all Donors\n"
      "R - Create a Report\n"
      "Q - Quit the Program"
      )

    menu_dict = {"T": thank_you, 
                 "L": letters_to_everyone, 
                 "R": create_report, 
                 "Q": quit_program
                 }

    while True:
        menu_selection = input("\nChoose a letter:  ")
        menu_selection = menu_selection.upper().strip()
        try:
            #can you remind me how the () here works?
            return menu_dict[menu_selection]()

            # if menu_selection == "T":
            #     thank_you()
            # elif menu_selection == "L":
            #     letters_to_everyone()
            # elif menu_selection == "R":
            #     create_report()
            # elif menu_selection == "Q":
            #     quit_program()

        #why is my exception not being raised here when I make an invalid entry?
        except (KeyError):
            print("Invalid response -- select T, R, or Q \n")
            return 
        #else:
            #pass
        #finally:
            #pass
       

def thank_you():
    print("\nMenu: Send a Thank You\n")
    thank_you_dict = {"list": donor_database,
                      "menu": main_menu,
                      "q": quit_program
                      }

    while True:
        donor_name = input("Enter the donor's full name. \n-- or 'list' to see a list of donors, \n-- or 'menu' to return to the main menu: ").strip()
        donor_name = donor_name.lower()
        try: 
            return thank_you_dict[donor_name]()

        # if donor_name == "list":
        #     print("\nDonor database:")
        #     for keys in donor_db:
        #         print(keys.title())
        #     print("\n")
        # elif donor_name == "menu":
        #     return main_menu()
        # elif donor_name == "q":
        #     return quit_program()
        # else:
        #     break
        except KeyError:
            print("Incorrect entry. Try again.")
            return
    donation_amount(donor_name)


def donation_amount(donor_name):
    while True:
        donor_amount = input("Enter amount of donation amount (or 'menu' to exit): ").strip()
        if donor_amount.lower() == "menu":
            return main_menu()
            #what is the difference between these three?...
               #return
               #return main_menu
               #return main_menu()
        elif donor_name.lower() == "q":
            return quit_program()
        else:
            break
    donor = find_donor(donor_name)
    if donor is None:
        donor_db[donor_name] = donor_amount
    print(ty_letter(donor_name, donor_amount))


def find_donor(donor_name):
    for donor in donor_db:
        if donor_name.strip().lower() == donor[0].lower():
            return donor
    return None


def ty_letter(donor_name, donor_amount):
    print("\nMenu: Send a Thank You, Letter\n")
    letter = (f"\nDear {donor_name.title()},\n\n\tYour donation of ${donor_amount} will make a great difference to a young learner at the coding academy. Thank you.\n\n\nSincerely,\nAn Academy Student\n")
    print(letter)
    print("--------------------------------\n\n")
    main_menu()


def letters_to_everyone():
    for donor_name in donor_db.values():
        letter = (f"\nDear {donor_name[0]},\n\n\tYour donation of ${donor_name[1][-1]} will make a great difference to a young learner at the coding academy. Thank you.\n\n\nSincerely,\nAn Academy Student\n")
        filename = donor_name[0].replace(" ", "_") + ".txt"
        print("Adressed to:", donor_name[0])
        open(filename, 'w').write(letter)
        print(letter)
        print("--------------------------------\n\n")
    return main_menu()


def create_report():
    report_rows = []
    for donor_name, values in donor_db.values():
        total_donations = sum(values)
        num_donations = len(values)
        avg_donations = total_donations / num_donations
        report_rows.append((donor_name, total_donations, num_donations, avg_donations))

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

