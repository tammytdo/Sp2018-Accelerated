'''
Jay Johnson
simple mail room
'''
import sys

donors = [("Donor A", [50,100,25,100]),
         ("Donor B", [50,100,25,100]),
         ("Donor C", [50,100,25,100]),
         ]



def thank_you():
    print("thank you")
    #If the user (you) selects ‘Send a Thank You’, prompt for a Full Name.
    #If the user types ‘list’, show them a list of the donor names and re-prompt
    #If the user types a name not in the list, add that name to the data structure and use it.
    #If the user types a name in the list, use it.
    #Once a name has been selected, prompt for a donation amount.
    #Turn the amount into a number – it is OK at this point for the program to crash if someone types a bogus amount.
    #Once an amount has been given, add that amount to the donation history of the selected user.
    #Finally, use string formatting to compose an email thanking the donor for their generous donation. Print the email to the terminal and return to the original prompt.
    #It is fine (for now) to forget new donors once the script quits running.

def report():
    print("report")

def quit():
    #prompt to ask if you really want to quit
    sys.exit()


def mainloop():
    print("Welcome to MailroomTM")

    response = ""
    while True:
        print("What do you want to do?")
        print("1) thank you,\n"
            "2) report,\n"
            "3) quit")
        response = input(">> ")

        #print("response was:" + response)
        if response not in ("1","2","3"):
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

if __name__ == '__main__':
    mainloop()
