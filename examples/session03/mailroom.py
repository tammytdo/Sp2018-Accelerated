#!/usr/bin/env python

"""
simple mailroom program for a non profit
"""

import sys

donors = [("Donor A", [50, 100, 25, 100]),
          ("Donor B", [100, 25,]),
          ("Donor C", [50, 100, 100]),
          ]


def thank_you():
    print("This is th thanks you function\n")


def report():
    print("This is the report function\n")


def quit():
    sys.exit()


def mainloop():
    print("Welcome to Mailroom")

    while True:
        print("What do you want to do?")
        print("1) thank you\n"
              "2) report\n"
              "3) quit\n")
        response = input(">> ")

        if response not in ("1", "2", "3"):
            print("*** Not a Valid response -- type 1,2,3 ***\n")
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

