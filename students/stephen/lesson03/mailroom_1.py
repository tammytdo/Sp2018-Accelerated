"""
Simple Mailroom Program for a nonprofit
"""

# The script should prompt the user (you) to choose from a menu of 3 actions:
# “Send a Thank You”, “Create a Report” or “quit”)

# Interactive Loop
import sys

# Create a data object to store donor information
donors = [('Jeff Bezos', [50, 100, 56]),
          ('Mark Zuckerberg', [45, 105, 349, 101, 78]),
          ('Paul Allen', [10, 50, 400, 400]),
          ('Elon Musk', [16, 68, 170, 425]),
          ('Richard Branson', [25, 90, 124, 300])
          ]


def names():
    """
    Refreshes the names list with current donors
    """
    names = []
    for tup in donors:
        names.append(tup[0])
    return names


# Sending a Thank You
# If the user (you) selects ‘Send a Thank You’, prompt for a Full Name.
# If the user types ‘list’, show them a list of the donor names and re-prompt
# If the user types a name not in the list, add that name to the data structure and use it.
# If the user types a name in the list, use it.
# Once a name has been selected, prompt for a donation amount.
# Turn the amount into a number – it is OK at this point for the program to crash if someone types a bogus amount.
# Once an amount has been given, add that amount to the donation history of the selected user.
# Finally, use string formatting to compose an email thanking the donor for their generous donation.
# Print the email to the terminal and return to the original prompt.

def thank_you():
    print()
    print('You have chosen Send a Thank You')
    ty_choice = ''
    while True:
        print('1) Enter the full name of the recipient\n2) See a list of donor names\n3) Return to the Main Menu')
        ty_choice = input('>> ')
        if ty_choice not in ('1', '2', '3'):
                print('Not a valid response. Type 1, 2, or 3\n')
                continue
        elif ty_choice == '1':
            print()
            print('Enter the full name of the recipient:')
            ty_name = input('>> ')
            print('Enter a donation amount:')
            ty_amount = input('>> ')
            print()
            enter_name(ty_name, ty_amount)
        elif ty_choice == '2':
            print()
            print('Donors:')
            for name in names():
                print(name)
            print()
            continue
        elif ty_choice == '3':
            print()
            mainloop()

def enter_name(name, amount):
    amount = float(amount)
    if name in names():
        donors[names().index(name)][1].append(amount)
    else:
        donors.append((name, [amount]))
    print("Dear {:s},\nWe greatly appreciate your generous donation of ${:.2f}.\nThank you,\nThe Team".format(name, amount))
    print()
    mainloop()

def avg_tup(tup):
    return sum(tup[1]) / len(tup[1])

def sum_tup(tup):
    return sum(tup[1])

def report():
    print('Donor Name                | Total Given | Num Gifts | Average Gift')
    print('------------------------------------------------------------------')
    sorted_donors = donors[:]
    sorted_donors.sort(key=sum_tup, reverse=True)
    for d in sorted_donors:
        print('{:26s} ${:>11.2f}  {:>10d}  ${:>11.2f}'.format(d[0], sum(d[1]), len(d[1]), avg_tup(d)))
    print()
    mainloop()

def quit():
    sys.exit()

def mainloop():
    print('Welcome to Mailroom')
    response = ''
    while True:
        print('What do you want to do?')
        print('1) Send a Thank You\n2) Create a Report\n3) Quit')
        response = input('>> ')
        print('Response was: ', response)
        print()
        if response not in ('1', '2', '3'):
            print('Not a valid response. Type 1, 2, or 3\n')
            continue
        elif response == '1':
            thank_you()
        elif response == '2':
            report()
        elif response == '3':
            quit()


if __name__ == '__main__':
    mainloop()
