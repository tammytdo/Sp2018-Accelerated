#! /usr/bin/env python3

import sys
import string

old_datas = [['William Gates III',  653784.39, 0],
         ['Mark Zuckerberg', 16396.10, 0, 0],
         ['Jeff Bezos', 877.33],
         ['Paul Allen', 708.42, 0, 0]]


donors_name = []
donations = []
for data in old_datas:
    donors_name.append(data[0])
    donations.append(data[1:])
datas = dict(zip((donors_name), donations))


#make a donors' name list
def donors_name_list():
    donors = datas.keys()
    return donors


def find_donor(donor):
    if donor not in datas:
        datas[donor] = []
    amount = input('Enter donation amount: ')
    try:
        amount = float(amount)
    except ValueError:
        print('error: donation amount is invalid\n')
    data[donor].append(amount)
    return datas


def letter(donor, amount):
    letter = '''Dear {}
        Thank you for your generous donation of ${:.2f}.
        We appreciate your contribution.
        Team R '''.format(donor, amount)
    print(letter)
    return letter


def thank_you():
    name = input("Enter donor's name or type 'list' to see all donors ").title()
    if name.lower() == 'list':
        print(donors_name_list())
    else:
        n_datas = find_donor(name)
        amt = n_datas[name][-1]
        letter(name, amt)
    print('\n<return to main menu>\n')



def pack(d):
    name, donation = d
    total = sum(donation)
    return (name, total, len(donation), (total / len(donation)))


def report():
    first_row = '{:20}|{:20}|{:10}|{:20}|'.format('Donor Name','Total Given', 'Num Gifts','Average Gifts')
    print(first_row)
    print('-'*len(first_row))
    donor_report = sorted([pack(data) for data in datas.items()],
                          key=lambda y: y[1], reverse=True)
    for data in donor_report:
        print(f"{data[0]:20}|${data[1]:19,.2f}|{data[2]:10}|${data[2]:19,.2f}|")
    print('\n<return to main menu>\n')
    return donor_report


def letters():
    datas = report()
    for data in datas:
        f_name = data[0]+'.txt'
        with open(f_name, 'wt') as f:
            print(f'''Dear {data[0]},
                Thank you for your generous donation ${data[1]:.2f}.
                We appreciate your contribution.
                Team R ''', file = f)



def quit():
    print('Exit Now')
    sys.exit()




def welcome():
    print('welcome to Mailroom')
    menu = {'1': thank_you, '2': report, '3': letters, '4': quit}
    while True:
        print('\nwhat do you want to do?')
        print('1) Send than you\n'
              '2) Creat a report\n'
              '3) Send letters to everyone\n'
              '4) quit\n')
        response = input('>> ')
        menu.get(response)()


if __name__ == "__main__":
    welcome()
