#! /usr/bin/env python3

''' simple mailroom proram for a non profit'''

import sys

datas = [['William Gates III',  653784.39, 2],
         ['Mark Zuckerberg', 16396.10, 3],
         ['Jeff Bezos', 877.33, 1],
         ['Paul Allen', 708.42, 3]]

#make a donors' name list
def donors_name_list():
    donors = []
    for data in datas:
        donors.append(data[0])
    return donors


def find_donor(donor,donors):
    '''find if donor is already in the datas, if not add the name to the datas'''
    donor = donor.rstrip().title()
    if donor in donors:
        return donor
    else:
        datas.append([donor, 0, 0])
        return donor

def upgrade_datas(donor):
    amount = float(input('Enter donation amount: ').rstrip())
    for data in datas:
        if donor == data[0]:
            data[1] += amount
            data[2] += 1
    return amount

def letter(donor, amount):
    print('''Dear {}
    Thank you for your generous donation of ${:.2f}.
    We very appreciate your contribution.
    Team R '''.format(donor, amount))


def thank_you():
    name = input("Enter donor's name or type 'list' to see all donors ").title()
    if name.lower() == 'list':
        print(donors_name_list())
    else:
        am = upgrade_datas(find_donor(name,donors_name_list()))
        letter(name, am)
        #letter(name, amount)
    print('\n<return to main menu>\n')





def report():
    report = []
    first_row = '{:20}|{:20}|{:10}|{:20}|'.format('Donor Name','Total Given', 'Num Gifts','Average Gifts')
    print(first_row)
    print('-'*len(first_row))
    for data in datas:
        row = '{:20}|{:20.2f}|{:10}|{:20.2f}|'.format(data[0],data[1],data[2],(data[1]/data[2]))
        print(row)
    print('\n<return to main menu>\n')


def quit():
    print('Exit Now')
    sys.exit()

def mainloop():
    print('welcome to Mailroom')

    while True:
        print('\nwhat do you want to do?')
        print('1) than you\n'
              '2) report\n'
              '3) quit\n')
        response = input('>> ')

        if response not in ('1', '2', '3'):
            print('***Not a valid response -- type 1,2,3***\n')
            continue
        elif response == '1':
            thank_you()
        elif response == '2':
            report()
        elif response == '3':
            quit()



if __name__ == '__main__':
    mainloop()
