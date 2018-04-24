#!/usr/bin/env python

'''
simple mailroom program
'''

import sys

donors = [('Donor A', [50, 100, 25, 100]),
          ('Donor B', [100, 25]),
          ('Donor C', [300])
          ]

def thank_you():
    #create list of donor names
    donor_name = []
    for (donor, amounts) in donors:
        donor_name.append(donor)
    while True:
        print('What do you want to do?')
        print('1. See list of donors\n'
              '2. Add donation to list\n'
              '3. Quit\n')

        response = input('>> ')
        if response = '1':
            print('List of donors:\n', donor_name, '\n')
        elif response = '2':
            print('Enter a name')

            name = input('>> ')
            if name in donor_name:
                print('Enter an amount')
                amount = int(input('>> '))
                for (donor, amounts) in donors:
                    if name = donor:
                        amounts.append(amount)
            else:
                print('Enter an amount')
                amount = int(input('>> '))
                donors.append((name, [amount]))
            print('{},\n\nThank you so much for you contribution of {}.'.format(name, amount))
        elif response = '3':
            quit()

def totaldonations(donations):
    return donations[1]

def report():
    report = []
    for (donor, amounts) in donors:
        report.append((donor, sum(amounts), len(amounts), sum(amounts)/len(amounts)))
    report.sort(key = totaldonations, reverse = True)
    print('Donor Name',' '*10, '|  Total Given  |', ' Num Gifts ', '|  Average Gift  |')
    print('-'*70)
    for (donor, total, num, avg) in report:
        print(donor, ' '*(21 - len(str(donor))), #print donor
              '$', ' '*(12 - len(str(total))), total, #print sum
              ' '*(12 - len(str(num))), num, #print num
              ' $', ' '*(12 - len(str(avg))), avg #print avg
             )

def letter():
    for (donor, amounts) in donors:
        outfile = open(donor + '.txt', 'w')
        outfile.write('Dear {},\n\n'.format(donor)
                      'Thank you for you donations of {}\n\n'.format(sum(amounts))
                      'Sincerly,\n-Me'
                      )
        outfile.close()

def mainloop():
    print('Welcome to the mailroom')

def quit():
    sys.exit()

    response = ''
    while True:
        print('What do you want to do?')
        print('1. Thank You\n'
              '2. Report\n'
              '3. Send Out Letters'
              '4. Quit\n')
        response = input('>> ')

        if response not in ('1', '2', '3'):
            print('Not a valid input: type 1, 2, or 3')
            continue
        elif response == '1':
            thank_you()
            continue
        elif response == '2':
            report()
            continue
        elif response == '3':
            letter()
            continue
        elif response == '4':
            quit()
            continue

if __name__ == '__main__'
    mainloop()
