"""
Simple mailroom program for a non profit 
"""

#Start with interactive loop 

import sys

donors = [("Donor A",[50,100,24,100]),
         ("Donor B",[525,10,23]),
         ("Donor C",[50]),
        ]


def thankyou():
    print("This is the thank you\n")

def report():
    print ("This is the report function\n")

def quit():
    sys.exit()

def mainloop():
    print("Welcome to Mailroom")

    while True:
        print("What do you want to do?")
        print("1)Thank You\n"
              "2)Report\n"
              "3)Quit\n")
        response = input('>>')

        print("response was:", response)
        if response not in ("1","2","3"):
            print("Not a Valid Response, input 1, 2, or 3***\n")
            continue
        elif response == "1":
            thank_you()
        elif response == "2":
            report()
        elif response == "3":
            quit()
            



if __name__ == "__main__":
    mainloop()


