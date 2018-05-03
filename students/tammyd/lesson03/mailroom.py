#!/usr/bin/env python

"""
simple mailroom program for a non profit
"""
import sys

donors = [("Britney Spears", [50, 100, 25, 100]),
          ("Christina Aguilera", [50, 100, 25, 100]),
          ("Mandy Moore", [50, 100, 25, 100]),
          ]


def thank_you():
    print("This is the thank you function")

def report():
    print("This is the report function")

def quit():
    print("Exited program")
    sys.exit()

def mainloop():
    print("Welcome to Mailroom")

    response = ""
    while response != "3":
        print("What do you want to do?")
        print(
          "1) Thank you\n"
          "2) Report\n"
          "3) Quit"
          )
        response = input("Choose a number:  ")

        if response not in ("1", "2", "3"):
            print ("*** Invalid response -- type 1,2,3 ***")
            continue
        elif response == "1":
            thank_you()
            continue
        elif response == "2":
            report()
            continue
        elif response == "3":
            quit()
            continue

if __name__ == "__main__":
    mainloop()