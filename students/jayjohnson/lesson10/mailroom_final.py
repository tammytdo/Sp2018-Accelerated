#!/usr/bin/env python3
'''
Dwight Johnson - MailRoom - Final
'''
import sys
from textwrap import dedent  # nifty utility!
import math


class MailRoom:
    def __init__(self, name, balance=0.0):
        self.name = name
        self._balance = []
        self._balance.append(float(balance))

    def deposit(self, amount):
        """make a deposit"""
        self._balance.append(float(amount))

    def donation_sum(self):
        """sum donation totals together"""
        return print("Total donations: $" + str(sum(self._balance)))

    # def create_donor_list(self):
    #     return

    @property
    def balance(self):
        """check the donation balance"""
        return self._balance

    @property
    def identity(self):
        """check the name"""
        return self.name

    # offical string repesentation
    def __repr__(self):
        return '{0.__class__.__name__}(name={0.name}, balance={0.balance})'.format(self)

    # informal string representation
    def __str__(self):
        return 'Donation totals for {}, current donations: {}'.format(self.name, self.balance)

    def __name__(self):
        return self.name

#print(donor2)
#print(donor2.balance)
#donor2.deposit(1000)
# print(str(donor1))
# print(repr(donor1))
# # print all donors
# print(donor1)
#print(donor2)
# print(donor3)


#
# def report():
#     print(donor1)
#     print(donor2)
#     print(donor3)
#def print_donors():
    #print(donor_new)
#print_donors()


def mainloop():

    #build donorlist
    donor1 = MailRoom('BILL', 100.00)
    donor2 = MailRoom('Alex', 2000.00)
    donor3 = MailRoom('Sam', 300000.00)
    donor1.deposit(50.00)
    donor1.deposit(20.00)
    donor2.deposit(5000.00)
    donor2.deposit(10000.00)
    donor3.deposit(1000000.00)
    donor3.deposit(50000.00)

    donor_db = []

    # add donors to database
    donor_db.append(donor1)
    donor_db.append(donor2)
    donor_db.append(donor3)
    #print(repr(donor_db[0]))
    #print(donor_db[1])
    #print(donor_db[2])
    #print(repr(donor_db))
    #print(repr(donor_db[0]))


    # print(donor_db[0].name)
    # print(donor_db[0].balance)
    #
    #
    #
    # #(donor_db[0].balance).deposit(1000.00)
    #
    #
    # donor_db[0].deposit(1000.00)
    #
    #
    # print(donor_db[0].balance)
    #
    #
    # # print(donor1)
    # name_game = "bill"
    # fake_donation = 1000
    #
    # i = 0
    #
    # if name_game in donor_db[i].name.lower():
    #     print(donor_db[i].name)
    #     print(donor_db[i].balance)
    #     donor_db[i].deposit(1000.00)
    #     print(donor_db[i].balance)

    # print(donor2)
    # print(donor3)
    # print(donor2.donation_sum())
    # print(str(donor1))
    # print(repr(donor1))
    # print(dir(donor1))

    def report():
        #print(donor_db)
        # this can be reduced
        i = 0

        while i < len(donor_db):
            name = (donor_db[i].name)
            total_letter_donation = (sum((donor_db[i]).balance))
            #donations = (len(donor_db[i].balance))
            i = i + 1

            print(dedent('''Dear {0:s},

            Thank you for your very kind donations totalling ${1:.2f}.
            It will be put to very good use.

                         Sincerely,
                            -The Team
                    '''.format(name, total_letter_donation)))

    def save_to_disk():
        # this can be reduced
        i = 0

        while i < len(donor_db):
            name_new = (donor_db[i].name)
            total_letter_donation = (sum((donor_db[i]).balance))
            #donations = (len(donor_db[i].balance))
            i = i + 1

            letter = []

            letter = (dedent('''Dear {0:s},

            Thank you for your very kind donations totalling ${1:.2f}.
            It will be put to very good use.

                         Sincerely,
                            -The Team
                    '''.format(name_new, total_letter_donation)))

            filename = name_new.replace(" ", "_") + ".txt"
            print("writting letter to:", name_new)
            open(filename, 'w').write(letter)


    def thank_you():
        # loop for donation name selection
        while True:
            name = input("Enter a donor's name or 'list' to see all donors or 'menu' to exit: ")
            if name == "list":
                report()
            elif name == "menu":
                return
            else:
                break

        amount = input("Amount to donate: ")

        # search list to see if donor name already exists
        # if name.strip().lower() in repr(donor_db[0]).lower():
        #     print("Name exists")
        #     #donor_db.append(float(amount))
        #     (donor_db[0].balance).deposit(1000.00)
        # else:
        #     print("name doesnt exist")
        i = 0
        new_donor_switch = True

        while i < len(donor_db):
            if name in donor_db[i].name.lower():
                #print(donor_db[i].name)
                #print(donor_db[i].balance)
                donor_db[i].deposit(amount)
                print(str(donor_db[i]))
                #print(donor_db[i].balance)
                i = i + 1
                # create switch here to determine if a new donor need to be created
                new_donor_switch = False
            else:
                i = i + 1

        if new_donor_switch == True:
            # creates a new donor
            donor_new = MailRoom(name, amount)
            print(str(donor_new))
            # #print(dir(donor_db))
            donor_db.append(donor_new)

        # doesnt work
        # if any(name in s for s in donor_db):
        #     print("its in the list")
        # else:
        #     print("its not in the list")

        # donor_new = MailRoom(name, amount)
        # print(str(donor_new))
        # #print(dir(donor_db))
        # donor_db.append(donor_new)

    print("Welcome to the MailRoom!")

    response = ""
    while True:
        print("What do you want to do?")
        print("1) Send a thank you,\n"
            "2) Create a report,\n"
            "3) Save reports to disk,\n"
            "4) quit")
        response = input(">> ")

        if response not in ("1","2","3","4"):
            print("Not a Valid response -- type 1,2,3,4")
            continue
        elif response == "1":
            thank_you()
            continue
        elif response == "2":
            report()
            # print(donor1)
            # print(donor2)
            # print(donor3)
            continue
        elif response == "3":
            save_to_disk()
        elif response == "4":
            quit()

if __name__ == '__main__':
    mainloop()
