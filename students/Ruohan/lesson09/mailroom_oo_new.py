#!/usr/bin/env python3


import sys
import string
from functools import reduce


class Donor():

    def __init__(self, name):
        self.name = name.capitalize()
        self.donation = []

    def add_donations(self, amount):
        self.donation.append(amount)

    @property
    def total(self):
        return sum(self.donation)


    @property
    def times(self):
        return len(self.donation)

    @property
    def ave(self):
        return self.total/self.times

    @property
    def last(self):
        if len(self.donation) > 0:
            return self.donation[-1]
        else:
            return 0

    def __str__(self):
        return f'{self.name}:{self.donation}'



class donor_DB():
    def __init__(self):
        self._donors = {}

    def find_donor(self, name):
        if name.lower() in self._donors:
            return self._donors[name.lower()]
        return None

    def add_donor(self, name):
        if self.find_donor(name):
            pass
        else:
            donor = Donor(name)
            self._donors[donor.name.lower()] = donor

    def search_donor(self,name):
        return self._donors.get(name.lower())

    def donor_list(self):
        return list(self._donors)

    def _letter(self, d):
        letter = f'''Dear {d.name}
            Thank you for your generous donation of ${d.last:.2f}.
            We appreciate your contribution.
            Team R '''
        return letter

    def report(self):
        head = '{:20}|{:20}|{:10}|{:20}|'.format('Donor Name','Total Given', 'Num Gifts','Average Gifts')
        result = [head]
        result.append('-'*len(head))
        for donor in self._donors:
            result.append(f"{donor.name:20}|${donor.total:19,.2f}|{donor.times:10}|${donor.ave:19,.2f}|")
        return result

    def file_letters(self):
        for donor in self._donors:
            f_name = donor.name+'.txt'
            with open(f_name, 'wt') as f:
                print(f'''Dear {donor.name},
                    Thank you for your generous donation ${donor.total:.2f}.
                    We appreciate your contribution.
                    Team R ''', file = f)

    def quit(self):
        sys.exit()

    def challenge(self, n, min_d = None, max_d = None):
        for donor in self._donors.values():
            if min_d is None and max_d is not None:
                donor.donation = list(filter(lambda x: x <= max_d, donor.donation))
            if min_d is not None and max_d is None:
                donor.donation = list(filter(lambda x: x >= min_d, donor.donation))
            if not min_d is None and max_d is None:
                donor.donation = list(filter(lambda x: x >= min_d and x <= max_d, donor.donation))
            else:
                continue
            donor.donation = map(lambda x : x * n, donor.donation)
        return self._donors

def Welcome():
    print('Welcome to Mailroom')
    db = donor_DB()
    while True:
        print('\nwhat do you want to do?')
        print('1) Check the donor list\n'
              '2) A new donation\n'
              '3) Send thank you\n'
              '4) Creat a report\n'
              '5) Send letters to everyone\n'
              '6) Total contribution by MORE\n'
              '7) quit\n')
        response = input('>> ')
        if response == '1':
            print(db.donor_list())
            print('Return to main menu\n')
        elif response == '2':
            name = input('Enter the donor name: ').lower()
            db.add_donor(name)
            amount = input('Enter the donation amount: ')
            try: amount = float(amount)
            except ValueError:
                print('error: donation amount is invalid\n')
            db.search_donor(name).add_donations(amount)
            print('New donation has been recorded')
            print('Return to main menu\n')
        elif response == '3':
            name = input('Who do you want to send thank you letter to: ').lower()
            if db.find_donor(name):
                print(db._letter(db.find_donor(name)))
            else:
                print('Donor is not recorded, please add donor to datasets first(chose 2 in main menu)\n')
                print('Return to main menu\n')
                continue
        elif response == '4':
            for line in db.report():
                print(line)
            print('Return to main menu\n')
        elif response == '5':
            db.file_letters()
            print('Letters have been saved')
            print('Return to main menu\n')
        elif response == '6':
            print('scenario 1: double contributions under $100\n'
                  'scenario 2: triple contributions over $50\n')
            rs = input('choose your scenario "1" or "2": ')
            if rs == '1':
                n = 2
                max = 100
                donor_new_data = db.challenge(n, max_d = max)
            elif rs == '2':
                n = 3
                min = 50
                donor_new_data = db.challenge(n, min_d = min)
            else:
                print('Invalid input')
            for donor in donor_new_data.values():
                print(donor.name,' new total donation is ', reduce(lambda x, y: x + y, donor.donation))
        elif response == '7':
            print('Exit Now')
            db.quit()
        else:
            print('Invalid input')
            print('Return to main menu\n')
            continue


if __name__ == "__main__":
    Welcome()
