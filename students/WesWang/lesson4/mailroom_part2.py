#=========================================================================================
#Name: Mailroom
#Author: Wesley Wang
#Date: 4/23/2018
#=========================================================================================

"""
Mailroom Part2
"""
import sys

donors = {"Donor A":[100000, 40000]
        , "Donor B":[1000]
        , "Donor C":[1000,1000,1000]
        , "Donor D":[5000,10000,5000]}


def thank_letter(donor, amount):
    print("-"*80)
    print(f"Dear {donor},\n\n\tWe have received you donation of ${amount:,.2f}. We greatly appreciate your generous contribution. This donation is meaningful and crucial to our organization's misson.\n\n\nSincerely,\n\nWesley Wang\n")
    print("-"*80)

def thank_you():
    # Ask for user input
    response = input("Please enter donor's full name, or type 'list' to check all donors: ").title()
    if response.lower() == "list":
        print("-"*20 + "\nList of Donors:\n" + "-"*20)
        for donor in donors.keys():
            print(donor)
        print("-"*20)
        thank_you()
    amount = int(input("Please enter donation amount for " + response + ":"))
    for donor in donors.keys():
        if response.lower() == donor.lower():
            donors[donor].append(amount)
            thank_letter(donor, amount)
            print("Return to main menu!!")
            mainloop()
    donors[response] = [amount]
    thank_letter(response, amount)
    mainloop()


def report():
    header = "{:30}| {:15}| {:10}| {:20}".format("Donor Name","Total Given", "Num Gifts","Average Gifts")
    print("-"*75)
    print(header)
    print("-"*75)

    for donor in donors.keys():
        total = 0
        giftnum = 0
        for gift in donors[donor]:
            total += gift
            giftnum += 1
        print(f"{donor:30}${total:>15,.2f}{giftnum:>13}{total/giftnum:>15,.2f}")
    print("-"*75)

def quit():
    print("You have successfully quit Mailroom")
    sys.exit()

def mainloop():
    print("Welcome to the Mailroom")

    response = ""
    while True:
        print("What do you want to do?")
        response = input("[1] Thank you\n[2] Report\n[3] Quit\n")
        print(response, " was chosen")

        if response not in ("1","2","3"):
            print("Not a Valid Response --- Type 1,2,3")
        elif response == "1":
            thank_you()
        elif response == "2":
            report()
        else:
            quit()


if __name__ == "__main__":
    mainloop()
