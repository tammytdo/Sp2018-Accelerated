import sys
from textwrap import dedent  # nifty utility!
import math

class MailRoom:
    def __init__(self, name, balance):
        self.name = name
        self._balance = []
        self._balance.append(float(balance))

    def deposit(self, amount):
        """make a deposit"""
        self._balance.append(float(amount))

    def donation_sum(self):
        """ sum donation totals together"""
        return print("Total donations: $" + str(sum(self._balance)))

    # def create_donor_list(self):
    #     return

    @property
    def balance(self):
        """check the donation balance"""
        return self._balance

    # offical string repesentation
    def __repr__(self):
        return '{0.__class__.__name__}(name={0.name}, balance={0.balance})'.format(self)

    # informal string representation
    def __str__(self):
        return 'Donation totals for {}, current donations: {}'.format(self.name, self.balance)

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
    donor1 = MailRoom('Jim Brokebuttrying', 100.00)
    donor2 = MailRoom('Alex Shouldgivemore', 2000.00)
    donor3 = MailRoom('Sam Worthalot', 300000.00)
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

    #print(donor_db)

    # print(donor1)
    # print(donor2)
    # print(donor3)
    # print(donor2.donation_sum())
    # print(str(donor1))
    # print(repr(donor1))
    # print(dir(donor1))

    def report():
        print(donor_db)

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
        donor_new = MailRoom(name, amount)
        print(str(donor_new))
        donor_db.append(donor_new)


    print("Welcome to the MailRoom!")

    response = ""
    while True:
        print("What do you want to do?")
        print("1) Send a thank you,\n"
            "2) Create a report,\n"
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
            # print(donor1)
            # print(donor2)
            # print(donor3)
            continue
        elif response == "3":
            quit()

if __name__ == '__main__':
    mainloop()
