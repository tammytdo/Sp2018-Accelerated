#!/usr/bin/env python

'''
simple mailroom program for a non profit
'''
import sys

donors = [("Donor A", [10, 20, 30, 40]),
          ("Donor B", [50, 60, 70, 80]),
          ("Donor C", [90, 100, 110, 120])]

donordict = {'Donor': ['Andrew Wall', 'Jeff Bezos', 'Bill Gates'],
             'Donation': [100, 260, 420]}


def thank_you():
    ty_letter = input("Please enter the full name of the donor\n"
                      "Or type 'list' to view donor name list:  ")
    if ty_letter == 'list':  # Works
        print("\nDonor List")
        print("----------")
        for items in donors:
            print("{: ^10s}".format(items[0]))
        print()
        thank_you()
    else:
        i = 0
        while i < 1:
            for item in donors:
                DonorInList = False
                if item[0].count(ty_letter) == 1:
                    DonorInList = True  # works
                    break
            if DonorInList is True:
                j = 0
                for item in donors:
                    if ty_letter == item[0]:  # Works
                        DonationVal = input("Donor found,\n\
How much was their donate?  ")
                        donorprof = donors[j]
                        vallist = donorprof[1]
                        DonationVal = int(DonationVal)
                        vallist.append(DonationVal)
                        print()
                        print(ty_letter, "\b's donation has been added to \
                              the Donor Report...Creating 'Thank you email'")
                        i = 1
                        One_letter(ty_letter, DonationVal)
                        mainloop()
                        break
                    else:
                        j += 1
            else:  # WORKS
                DonationVal = input("Adding Donor to list,\n\
How much was their donate?  ")
                DonationVal = int(DonationVal)
                vallist = []
                vallist.append(DonationVal)
                Don_Val = ()
                Don_Val = (ty_letter[:], vallist[:])
                donors.append(Don_Val)
                print()
                print(ty_letter, "and their donation have been added to the \
                      Donor Report...Creating 'Thank you email'")
                i = 1
                One_letter(ty_letter, DonationVal)
                mainloop()
                break  # Works


def One_letter(donor, donation):
    print()
    print("Dear {};\n\n\t Thank you for your generous donation of ${:.2f}.\n\n \
\tSincerely,\n\n \tThe Python Project\n".format(donor, donation))  # Works


def All_letters(donordict):
    donorvallist = list(donordict.values())
    for i in range(len(donorvallist[0])):
        Donor, Donation = donordict['Donor'][i], donordict['Donation'][i]
        Donation = int(Donation)
        # could not figure out a way to unpack the dictionary (like Mr. Barker
        # suggested in the question) with multiple values per key, since you
        # can not use [i] because it needs to be a int not a string
        lettertemplate = ("Dear {},\n\n\
        Thank you for your very kind donation of ${:,.02f}. \
        \n\n\t\t Sincerely,\n\t\t  -The Team".format(Donor, Donation))
        filename = open("{}.txt".format(Donor), 'w')
        filename.write(lettertemplate)
        filename.close()
    print("Creating 'Thank you' letters to all Donors")
    mainloop()


def report(donors):
    Repheader = ('Donor Name', 'Total Given', 'Num Gifts', 'Average Gifts')
    headerspace = '{:20}| {:^14}| {:^10}| {:^14}'
    ReportCats = headerspace.format(*Repheader)
    print('\n', ReportCats)
    print('-' * 63)
    for item in donors:
        print('{:20}| ${:^13,.02f}| {:^10}| ${:^14,.02f}'.format(item[0],
        sum(item[1]), len(item[1]), (sum(item[1]) / len(item[1]))))
    mainloop()


def quit():
    sys.exit()


def mainloop():
    print("\nWelcome to mailroom\n")
    while True:
        print("\nWhat do you want to do? ")
        print("1) Thank you\n"
              "2) View Report\n"
              "3) Send letters to everyone\n"
              "4) Quit\n")
        response = input('>>')

        if response not in ("1", "2", "3", "4"):
            print("***Not a Valid response  -- type 1,2,3***\n")
            continue
        elif response == "1":
            thank_you()
        elif response == "2":
            report(donors)
        elif response == "3":
            All_letters(donordict)
        elif response == "4":
            quit()


if __name__ == "__name__":
    mainloop()
    # thank_you()
    # letter()
