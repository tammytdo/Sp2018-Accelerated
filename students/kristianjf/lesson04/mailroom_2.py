#!/usr/bin/env python3

import sys
'''
Goal:
You work in the mail room at a local charity. Part of your job is to write \
incredibly boring, repetitive emails thanking your donors for their generous \
gifts. You are tired of doing this over and over again, so you’ve decided to \
let Python help you out of a jam and do your work for you.
'''
'''
It should have a data structure that holds a list of your donors and a history of \
the amounts they have donated. This structure should be populated at first with at \
least five donors, with between 1 and 3 donations each.
'''
DATA_STRUCTURE = [('Jeff Bezos', [200, 500, 1000]),
                    ('Bill Gates', [1000]),
                    ('Steve Jobs', [20, 50, 100])]

#PROGRAM_OPTIONS = ['Send a Thank You', 'Create a Report', 'Send letters to everyone', 'quit']

def menu(options_dict):
    '''
    The script should prompt the user (you) to choose from a menu of 3 actions: \
    “Send a Thank You”, “Create a Report” or “quit”)
    '''
    response = ''
    options = [option[0:2] for option in enumerate(options_dict.keys(), 1)]
    while True:
        print('Please select a number from the list of the following options: \n')
        for option in options:
            print(option)
        response = int(input())
        response_selection = options[response-1][1]
        options_dict[response_selection]()

def thank_you():
    '''
    Sending a Thank You
    If the user (you) selects ‘Send a Thank You’, prompt for a Full Name.
        If the user types a name not in the list, add that name to the data structure and use it.
        If the user types a name in the list, use it.
    If the user types ‘list’, show them a list of the donor names and re-prompt
    Once a name has been selected, prompt for a donation amount.
    Turn the amount into a number – it is OK at this point for the program to crash if \
    someone types a bogus amount.
    Once an amount has been given, add that amount to the donation history of the selected user.
    Finally, use string formatting to compose an email thanking the donor for their generous \
    donation. Print the email to the terminal and return to the original prompt.
    '''
    program_options_ty = ['Send a Thank You', 'action: list', 'quit']
    response = ''
    options = [option for option in enumerate(program_options_ty, 1)]
    while True:
        print('Menu: Send a Thank You')
        print('Please select a number or action from the list of the following options: \n')
        for option in options:
            print(option)
        response = input()
        if response == str(options[0][0]):
            full_name = input('Please enter full name of the recipient: ').split()
            '''
            Format Full name
            '''
            full_name_cap = ''
            for name in full_name:
                full_name_cap += f'{name.capitalize()} '
            full_name = full_name_cap.strip()
            '''
            Process Full Name
            '''
            ds_names = [name for name, donation in DATA_STRUCTURE]
            if full_name in ds_names:
                full_name_index = ds_names.index(full_name)
                print(f'Found {full_name} in data_structure')
                donation_amount = int(input('Please enter a donation amount: '))
                DATA_STRUCTURE[full_name_index][1].append(donation_amount)
                print(f'Dear {full_name},\n\nThank you for your generous donation of '
                      f'${donation_amount}. Please send us more money at your earliest '
                      f'convenience.')
                break
            else:
                donation_amount = int(input('Please enter a donation amount: '))
                DATA_STRUCTURE.append((full_name, [donation_amount]))
                print(f'Dear {full_name},\n\nThank you for your generous donation of '
                      f'${donation_amount}. Please send us more money at your earliest '
                      f'convenience.')
                break
        elif response in [str(options[1][0]), 'list']:
            for entry in DATA_STRUCTURE:
                print(entry)
        elif response == str(options[2][0]):
            break
        else:
            print('Invalid Response. Please Try Again.')

def create_a_report():
    '''
    Creating a Report
    If the user (you) selected “Create a Report”, print a list of your donors, \
    sorted by total historical donation amount.
    Include Donor Name, total donated, number of donations and average donation \
    amount as values in each row. You do not need to print out all their donations, \
    just the summary info.
    Using string formatting, format the output rows as nicely as possible. \
    The end result should be tabular (values in each column should align with those above and below)
    After printing this report, return to the original prompt.
    At any point, the user should be able to quit their current task and \
    return to the original prompt.
    From the original prompt, the user should be able to quit the script cleanly.
    Your report should look something like this:

    Donor Name                | Total Given | Num Gifts | Average Gift
    ------------------------------------------------------------------
    William Gates, III         $  653784.49           2  $   326892.24
    Mark Zuckerberg            $   16396.10           3  $     5465.37
    Jeff Bezos                 $     877.33           1  $      877.33
    Paul Allen                 $     708.42           3  $      236.14
    Donor_name = 30, Total Given = 20, Num Gifts = 10, Average Gift = 20
    '''
    print('Menu: Create a Report')
    top_row = ('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift')
    format_header = '{:<30} | {:<15} | {:<10} | {:<15}\n'
    format_data = '{:<30} {:>15}    {:^10} $ {:<15.2f}\n'
    format_string = format_header.format(*top_row)
    report = [format_string]
    for item in DATA_STRUCTURE:
        name = item[0]
        total_given = sum(item[1])
        num_gifts = len(item[1])
        avg_gift = sum(item[1]) / num_gifts
        report.append(format_data.format(name, "${:,.2f}".format(total_given), num_gifts, avg_gift))
    print("".join(report))

def send_letters(data_structure=DATA_STRUCTURE[:]):
    '''
    Try to use a dict and the .format() method to do the letter as one big \
    template rather than building up a big string in parts.
    Example:
    In [3]: d
    Out[3]: {'first_name': 'Chris', 'last_name': 'Barker'}

    In [5]: "My name is {first_name} {last_name}".format(**d)
    Out[5]: 'My name is Chris Barker'

    In this version, add a function (and a menu item to invoke it), that goes \
    through all the donors in your donor data structure, generates a thank you \
    letter, and writes it to disk as a text file.
    '''
    data_structure_list = []
    for name, donations in data_structure:
        data_structure_dict = {}
        data_structure_dict['name'] = name
        data_structure_dict['donation'] = donations[-1]
        data_structure_list.append(data_structure_dict)
    for entry in data_structure_list:
        filename = '_'.join(entry.get('name').split())+'.txt'
        print(filename)
        print(entry)
        with open(filename, 'w') as outfile:
            outfile.write('Dear {name},\n\nThank you for your very kind donation of '
                          '${donation:.2f}\n\nIt will be put to very good use.\n\n'
                          '{:' '<15}Sincerely, \n\n{:' '<15}-The Team'.format(' ', ' ', **entry,))

PROGRAM_OPTIONS_DICT = {'Send a Thank You': thank_you,
                        'Create a Report': create_a_report,
                        'Send Letters to Everyone': send_letters,
                        'quit': sys.exit}

if __name__ == '__main__':
    menu(PROGRAM_OPTIONS_DICT)
