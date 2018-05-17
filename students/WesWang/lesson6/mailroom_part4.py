#=========================================================================================
#Name: Mailroom part4
#Author: Wesley Wang
#Date: 5/13/2018
#=========================================================================================

"""
Mailroom Part4
"""
import sys
from datetime import date


donors = {"Donor A":[100000, 40000]
        , "Donor B":[1000]
        , "Donor C":[1000,1000,1000]
        , "Donor D":[5000,10000,5000]}


def thank_letter(donor, amount):
    letter = "-"*80 + f"""\nDear {donor},\n\n\tWe have received you donation of ${amount:,.2f}.
        \n\n\tWe greatly appreciate your generous contribution.
        \n\n\tThis donation is meaningful and crucial to our organization's misson.
        \n\nSincerely,\n\nWesley Wang\n""" + "-"*80
    return letter


def thank_you():
    # Ask for user input
    response = input("Please enter donor's full name, or type 'list' to check all donors: ").title()
    if response.lower() == "list":
        print("-"*20 + "\nList of Donors:\n" + "-"*20)
        for donor in sorted(donors):
            print(donor)
        print("-"*20)
        thank_you()

    while True:
        try:
            amount = float(input("Please enter donation amount for " + response + ":"))
            break
        except:
            print("\nPlease enter a dollar amount!!\n")
            continue

    for donor in donors:
        if response.lower() == donor.lower():
            donors[donor].append(amount)
            print(thank_letter(donor, amount))
            print("Return to main menu!!")
            mainloop()
    donors[response] = [amount]
    print(thank_letter(response, amount))
    return


def build_report():
    header = ["Donor Name","Total Given", "Num Gifts","Average Gifts"]
    report = ""
    report += "-"*75
    report += f"\n{header[0]:30}| {header[1]:15}| {header[2]:10}| {header[3]:20}\n"
    report += "-"*75
    for donor in donors:
        total = 0
        giftnum = 0
        for gift in donors[donor]:
            total += gift
            giftnum += 1
        report += f"\n{donor:30}${total:>15,.2f}{giftnum:>13}{total/giftnum:>15,.2f}"
    report += "\n" + "-"*75
    return report


def report():
    print(build_report())


def send_letters():
    file_path = "C:\_Python_210AC\Sp2018-Accelerated\students\WesWang\lesson6\\"
    for donor in donors:
        letters = open(file_path + donor.replace(" ", "_") + "_Donation_Letter_" + str(date.today()) + ".txt", "w")
        letters.write(thank_letter(donor, donors[donor][-1]))
        letters.close()
    print("\nLetters to all donors' previous donations printed !!\n")
    return


def quit():
    print("You have successfully quit Mailroom")
    sys.exit()

menu = {"1":["Send a Thank you", thank_you]
    , "2":["Create a Report", report]
    , "3":["Send Letters to Everyone", send_letters]
    , "4":["Quit", quit]}


def mainloop():
    print("\nWelcome to the Mailroom\n")

    while True:
        for key, value in menu.items():
            print("[" + key + "] "+ value[0])
        response = input("What do you want to do?\t")
        print(response, " was chosen")

        if response not in menu:
            print("Not a Valid Response --- Type 1, 2, 3, or 4")
        else:
            menu[response][1]()


if __name__ == "__main__":
    mainloop()
