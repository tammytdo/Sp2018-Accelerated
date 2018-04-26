#!/usr/bin/env python3
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
DATA_STRUCTURE = [('Jeff Bezos', [200, 500, 1000]), \
                    ('Bill Gates', [1000]), \
                    ('Steve Jobs', [20, 50, 100])]

PROGRAM_OPTIONS = ['Send a Thank You', 'Create a Report', 'quit']

def menu(options):
    '''
    The script should prompt the user (you) to choose from a menu of 3 actions: \
    “Send a Thank You”, “Create a Report” or “quit”)
    '''
    response = ''
    options = [option for option in enumerate(options, 1)]
    while True:
        print('Please select a number from the list of the following options: \n')
        for option in options:
            print(option)
        response = int(input())
        if response == options[0][0]:
            thank_you()
        elif response == options[1][0]:
            create_a_report()
        elif response == options[2][0]:
            break
        else:
            print('Invalid Response. Please Try Again.')

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
    format_data = '{:<30} $ {:<15.2f}   {:<10} $ {:<15.2f}\n'
    format_string = format_header.format(*top_row)
    for item in DATA_STRUCTURE:
        name = item[0]
        total_given = sum(item[1])
        num_gifts = len(item[1])
        avg_gift = sum(item[1]) / num_gifts
        format_string += format_data.format(name, total_given, num_gifts, avg_gift)
    print(format_string)

if __name__ == '__main__':
    menu(PROGRAM_OPTIONS)
