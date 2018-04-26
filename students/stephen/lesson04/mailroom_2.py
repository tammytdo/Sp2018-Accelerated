"""
Simple Mailroom Program for a nonprofit
"""

# The script should prompt the user (you) to choose from a menu of 3 actions:
# “Send a Thank You”, “Create a Report” or “quit”)

# Interactive Loop
import sys

# Create a data object to store donor information
donors = {
    'Jeff Bezos': [50, 100, 56],
    'Mark Zuckerberg': [45, 105, 349, 101, 78],
    'Paul Allen': [10, 50, 400, 400],
    'Elon Musk': [16, 68, 170, 425],
    'Richard Branson': [25, 90, 124, 300]
}


def names():
    """
    Refreshes the names list with current donors
    """
    names = []
    for tup in donors:
        names.append(tup[0])
    return names

def gen_letter(donor):
    return "Dear {:s},\n\nWe greatly appreciate your generous donation of ${:,.2f}.\n\nThank you,\nThe Team".format(donor[0], donor[1])

def write_letters_to_disk():
    """
    Generate one letter for each donor and write to disk
    """
    for n, d in donors.items():
        print('Generating letter to {:s}'.format(n))
        donor = (n, d[-1])
        letter = gen_letter(donor)
        filename = n.replace(' ', '_') + '.txt'
        with open(filename, 'w') as outfile:
            outfile.write(letter)
    print()
    return

def enter_name(name, amount):
    amount = float(amount)
    donors.setdefault(name, []).append(amount)
    print(gen_letter([name, amount]))
    print()

def get_name_donation():
    print('\nEnter the full name of the recipient:')
    ty_name = input('>> ')
    print('Enter a donation amount:')
    ty_amount = input('>> ')
    print()
    enter_name(ty_name, ty_amount)

def donor_list():
    print('\nDonors:')
    for name in donors:
        print(name)
    print()

def thank_you():
    print()
    print('You have chosen Send a Thank You')
    ty_choice = ''
    switch_func_dict = {
        '1': get_name_donation,
        '2': donor_list
    }
    while ty_choice != '3':
        print('1) Enter the full name of the recipient\n2) See a list of donor names\n3) Return to the Main Menu')
        ty_choice = input('>> ')
        try:
            switch_func_dict.get(ty_choice)()
        except TypeError:
            print('Not a valid response. Type 1, 2, or 3\n')
        continue
    return
        

def avg_tup(tup):
    return sum(tup[1]) / len(tup[1])

def sum_tup(tup):
    return sum(tup[1])

def report():
    print('Donor Name                | Total Given | Num Gifts | Average Gift')
    print('-' * 66)
    sorted_donors = list(donors.items())
    sorted_donors.sort(key=sum_tup, reverse=True)
    report_rows = []
    for d in sorted_donors:
        report_rows.append('{:26s} {:>12s} {:^13d} {:>12s}\n'.format(d[0], ('${:,.2f}'.format(sum(d[1]))), len(d[1]), ('${:,.2f}'.format(avg_tup(d)))))
    print(''.join(report_rows))
    return

def quit():
    sys.exit()

def mainloop():
    print('Welcome to Mailroom')
    response = ''
    switch_dict = {
        '1': thank_you,
        '2': report,
        '3': write_letters_to_disk,
        '4': quit
    }
    while response != '4':
        print('What do you want to do?')
        print('1) Send a Thank You\n2) Create a Report\n3) Send letters to everyone\n4) Quit')
        response = input('>> ')
        # print('Response was: {:s}\n'.format(response))
        try:
            switch_dict.get(response)()
        except TypeError:
            print('Not a valid response. Type 1, 2, 3, or 4\n')
        continue


if __name__ == '__main__':
    mainloop()
