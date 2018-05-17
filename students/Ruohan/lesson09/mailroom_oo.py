#!/usr/bin/env python3


import sys
import string


class Donor():

    def __init__(self, name):
        self.name = name
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

    def fIsDonor(self, name):
        return self.name == name


class Handle():

    def __init__(self):
        self.donordatas = []
        self.donors_name_list = []

    def __find_donor(self, name):
        for donor in self.donordatas:
            if donor.fIsDonor(name):
                return donor
        return None

    def add_donor(self, name):
        donor = Donor(name)
        if self.__find_donor(name):
            print('Donor is already in the datatsets')
        else:
            self.donordatas.append(donor)
        amount = input('Enter donation amount: ')
        try: amount = float(amount)
        except ValueError:
            print('error: donation amount is invalid\n')
        donor.add_donations(amount)
        return donor

    def search_donor(self, name):
        if self.__find_donor(name):
            print('Donor is already in the datasets\n')
        else:
            print('Donor is not in datasets, please add donor to the datasets')

    def donors_list(self):
        for donor in self.donordatas:
            self.donors_name_list.append(donor.name)
        return self.donors_name_list

    def _letter(self, d):
        letter = '''Dear {}
            Thank you for your generous donation of ${:.2f}.
            We appreciate your contribution.
            Team R '''.format(d.name, d.last)
        return letter

    def thank_you(self):
        name = input("Enter donor's name or type 'list' to see all donors: ").title()
        if name.lower() == 'list':
            print(self.donors_list())
        else:
            letter_data = self.add_donor(name)
            print(self._letter(letter_data))
        print('\n<return to main menu>\n')

    def report(self):
        first_row = '{:20}|{:20}|{:10}|{:20}|'.format('Donor Name','Total Given', 'Num Gifts','Average Gifts')
        print(first_row)
        print('-'*len(first_row))
        for donor in self.donordatas:
            print(f"{donor.name:20}|${donor.total:19,.2f}|{donor.times:10}|${donor.ave:19,.2f}|")
        print('\n<return to main menu>\n')


    def file_letters(self):
        for donor in self.donordatas:
            f_name = donor.name+'.txt'
            with open(f_name, 'wt') as f:
                print(f'''Dear {donor.name},
                    Thank you for your generous donation ${donor.total:.2f}.
                    We appreciate your contribution.
                    Team R ''', file = f)

    def quit(self):
        sys.exit()


if __name__ == "__main__":
    print('Welcome to Mailroom')
    p = Handle()
    while True:
        print('\nwhat do you want to do?')
        print('1) Send thank you\n'
              '2) Creat a report\n'
              '3) Send letters to everyone\n'
              '4) quit\n')
        response = input('>> ')
        menu = {'1': p.thank_you, '2': p.report, '3': p.file_letters, '4': p.quit}
        menu.get(response)()
