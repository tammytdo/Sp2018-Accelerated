#!/usr/bin/env python


"""
simple mailroom program for a non profit
"""



"""
original list of donors
donors = [("Donor A", [50, 100, 25, 100]),
                ("Donor B"), [50, 25]),
                ("Donor C"), [50, 100, 100]),
                ]

"""
#
#       Implementing cleaver student soluton for Dict-Switch **Brilliant!**
#       Source: https://github.com/mathewcmartin/Sp2018-Accelerated/blob/master
#       /solutions/Lesson05/mailroom_dict_switch.py
#

import sys

donors = ["John Smith", "Ringo Eclipse", "Burt Syran", "Lance J. Johnson", 
          "Orel Winfrey"]
dues = [[25, 25], [25, 25, 25, 25], [50, 50, 50, 150], [25, 25, 50, 25], [500]]

# Global variable for donors and dues paid

DONORS = dict(zip(donors, dues))
del donors
del dues

def thank_you():
    print("This is a thank_you function")


def report():
    print("This is a report function")

def quit():
    sys.exit()
    
def return_to_menu():
    """ returns true to exit out of subloop: from solutions"""
    return True


def mainloop():
    print("Welcome to Mailroom")

    response = ""
    while True:
        print("What do you want to do?")
        print("1) thank you\n"
                "2) report\n"
                "3) quit\n")
        response = input(">> ")

        if response not in ('1', '2', '3'):
            print("Not a Valid response -- type 1,2,3")
            continue
        elif response == "1":
            thank_you()
            continue
        elif response == "2":
            report()
            continue
        elif response == "3":
            quit()

if __name__ == "__main__":
    mainloop()
