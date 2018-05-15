#!/usr/bin/env python

"""

Assignment: Object Oriented Mailroom

Updating mailroom_pt4.py

"""


import sys

#Encapsulation
#Separation
#DRY
#You will have a method for each of the functions in your non-OO version. 

#pt1: data structure that holds a list of your donors
donor_db = {"Britney Spears": ("Britney Spears", [50.99, 100.99, 1000.99]),
            "Christina Aguilera": ("Christina Aguilera", [50.99, 100.99, 2000.99]),
            "Mandy Moore": ("Mandy Moore", [50.99, 100.99, 3000.99]),
            "Jessica Simpson": ("Jessica Simpson", [50.99, 100.99, 4000.99]),
            "Queen Bey": ("Queen Bey", [50.99, 100.99, 5000.99]),
            }


#You'll want a Donor class – this will hold all the information about the donor, and have attributes and methods to provide access to the donor specific information that is needed.
#method only needs the information from one donor
class Donor:
    #info about the donor
    def __init__(self, name, donations= None):
        self._name = name
        self._donations = [] if donations is None else donations
        # same as...
        # if donations is None:
        #     self._donations = []
        # else:
        #     self._donations = donations

    @property
    def name(self):
        return self._name

    @property
    def donations(self):
        return self._donations

    #pt1: a history of the amounts they have donated.
    @property
    def total_donations(self):
        return sum(self._donations)

    @property
    def new_donation(self, donation_amount):
        self._donations.append(donation_amount)

    @property
    # total_donations = sum(values)
    def total_donations(self):
        return sum(self._donations)

    @property
    # num_donations = len(values)
    def num_donations(self):
        return len(self._donations)

    @property
    # avg_donations = total_donations / num_donations
    def avg_donations(self):
        return sum(self._donations) / len(self._donations)




#You’ll then want a class that handles the collection of donors. 
#method needs the information from the whole collection.
#pt1: data structure that holds a list of your donors
#Do I want to include or exclude () right after DonorDB here?
class DonorDB:
    #donor objects
    def __init__(self):
        self._donors = {}

    def donor_database():
    #print("test: inside def donor_database")
        print("Donor list: \n")
        for donor in donor_db.keys():
            #tried many different ways to print the donors. what am I missing??
            #return donor[0] + "\n"
            #return donor_db
            #return donor_db.donor[0] + "\n"
            #return donor_db[0] + "\n"

    #methods to add a new donor
    def add_donor(self, donor):
        self._donors[donor.name.lower()] = donor
    #search for a given donors
    #save and re-load your data

#pt1: Send a Thank You
def thank_you():
    print("\nMenu: Send a Thank You\n")
    thank_you_dict = {"list": DonorDB.donor_database,
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


#pt1:Create a Report
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
    #can you remind me how to return without going deeper into the stack?
    return main_menu()


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
            return menu_dict[menu_selection]()
        #why is my exception not being raised here when I make an invalid entry?
        except KeyError:
            print("Invalid response -- select T, R, or Q \n") 
        #else:
            #pass
        #finally:
            #pass
       
 
#pt1: quit
def quit_program():
    print("You have exited the Mailroom.")
    sys.exit()


if __name__ == "__main__":
    mainloop()

