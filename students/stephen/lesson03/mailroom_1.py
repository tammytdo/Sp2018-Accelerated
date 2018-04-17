"""
Simple Mailroom Program for a nonprofit
"""

# The script should prompt the user (you) to choose from a menu of 3 actions:
# “Send a Thank You”, “Create a Report” or “quit”)

# Interactive Loop
import sys

# Create a data object to store donor information
donors = [('Donor A', [50, 100]),
          ('Donor B', [50, 100, 200, 100, 60]),
          ('Donor C', [10, 50, 400, 400]),
          ]


def thank_you():
    print('This is the thank_you() function')


def report():
    print('This is the report function')


def quit():
    sys.exit()


def mainloop():
    print('Welcome to Mailroom')
    response = ''
    while True:
        print('What do you want to do?')
        print('1) Send a Thank You\n2) Create a Report\n3) Quit')
        response = input('>>')
        print('Response was: ', response)
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
