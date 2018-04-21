"""
Simple mailroom program for a non profit 
"""

#Start with interactive loop 

import sys
from textwrap import dedent

donors = [("Donor A",[50,100,24,100]),
         ("Donor B",[525,10,23]),
         ("Donor C",[50]),
        ]


#def thankyou():
    #print("Please Input the Donor you would like to thank\n")


#Building Donor List 

def list_donors():
    print("Donors:\n")
    for donor in donors:
        print(donor[0])

def thankyou():
    while True:
        name = input("Enter the donor's name or a list of donor's"
                      "(names to see all donors or type 'menu' to exit)>").strip()
        if name == "list":
            list_donors()
        elif name == "menu":
            return
        else:
            break




def report():
    print("This is the report function\n")

def quit():
    sys.exit()

def mainloop():
    
    mainmenuinput = input(dedent("""
        What would you like to do?

        (1) - Send a Thank You Letter
        (2) - Build a Report
        (3) - Quit

        > """))
    return mainmenuinput.strip()


if __name__ == "__main__":
    running = True
    while running:
        response = mainloop()
        if response not in ('1', '2', '3'):
            print("Not a Valid Response, input 1, 2, or 3")
            continue
        elif response == '1':
            thankyou()
        elif response == '2':
            report()
        elif response == '3':
            quit()
