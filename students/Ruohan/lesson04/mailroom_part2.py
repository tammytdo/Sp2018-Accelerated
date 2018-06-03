#!/usr/bin/env python3

import sys
import string

old_datas = [['William Gates III',  653784.39, 2],
         ['Mark Zuckerberg', 16396.10, 3],
         ['Jeff Bezos', 877.33, 1],
         ['Paul Allen', 708.42, 3]]

# make a new data structure for part2
datas = []

for i in old_datas:
    dic = {}
    dic.setdefault('name', i[0])
    dic.setdefault('donation_amount', i[1])
    dic.setdefault('donation_times',i[2])
    dic.setdefault('recent_donation')
    datas.append(dic)


#make a donors' name list
def donors_name_list():
    donors = []
    for data in datas:
        donors.append(data['name'])
    return donors


def find_donor(donor,donors):
    '''find if donor is already in the datas, if not add the name to the datas'''
    if donor not in donors:
        donor_info = {'name': donor}
        donor_info.setdefault('donation_amount',0)
        donor_info.setdefault('donation_times', 0)
        datas.append(donor_info)
    return donor


def upgrade_datas(donor):
    # upgrade donors' total donation amount, donation times and recent donation amount
    amount = float(input('Enter donation amount: '))
    for data in datas:
        if donor == data.get('name'):
            data['donation_amount'] +=  amount
            data['donation_times'] += 1
            data.setdefault('recent_donation', amount)
    return datas

def letter(donor, amount):
    print('''Dear {}
        Thank you for your generous donation of ${:.2f}.
        We appreciate your contribution.
        Team R '''.format(donor, amount))


def thank_you():
    name = input("Enter donor's name or type 'list' to see all donors ").title()
    if name.lower() == 'list':
        print(donors_name_list())
    else:
        datas = upgrade_datas(find_donor(name, donors_name_list()))
        for data in datas:
            if name == data['name']:
                amt = data['recent_donation']
                letter(name, amt)
    print('\n<return to main menu>\n')


def report():
    first_row = '{:20}|{:20}|{:10}|{:20}|'.format('Donor Name','Total Given', 'Num Gifts','Average Gifts')
    print(first_row)
    print('-'*len(first_row))
    for data in datas:
        data.setdefault('Ave_amount', (data['donation_amount']/data['donation_times']))
        print(f"{data['name']:20}|${data['donation_amount']:19,.2f}|{data['donation_times']:10}|${data['Ave_amount']:19,.2f}|")
    print('\n<return to main menu>\n')




def letters():
    for data in datas:
        f_name = data['name']+'.txt'
        with open(f_name, 'wt') as f:
            print(f'''Dear {data['name']},
                Thank you for your generous donation ${data['donation_amount']:.2f}.
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
