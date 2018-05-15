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
class Donor:
    def __init__(self, name, donations):
        self._name = name
        self._normalized_name = ''
        self._donations = donations if isinstance(donations, list) else [donations]
    def __lt__(self, other):
        return sum(self.donations) < sum(other.donations)
    @property
    def name(self):
        return self._name
    @property
    def donations(self):
        return self._donations
    @property
    def normalized_name(self):
        'Validate and Return Name Input'
        full_name_cap = ''
        try:
            for name in self.name.split():
                assert name.isalpha()
                full_name_cap += f'{name.capitalize()} '
            full_name = full_name_cap.strip()
        except AssertionError:
            print('Invalid Name. Found non-alphabetic characters')
        else:
            return full_name
        return self._normalized_name
    def donate(self, new_donation):
        self.donations.append(new_donation)
    def metrics(self):
        num_d = len(self.donations)
        total_d = sum(self.donations)
        avg_d = total_d / num_d
        return num_d, total_d, avg_d

    def send_letter(self):
        '''
        Try to use a dict and the .format() method to do the letter as one big \
        template rather than building up a big string in parts.
        In this version, add a function (and a menu item to invoke it), that goes \
        through all the donors in your donor data structure, generates a thank you \
        letter, and writes it to disk as a text file.
        '''
        filename = '_'.join(self.name.split())+'.txt'
        with open(filename, 'w') as outfile:
            outfile.write(self.output_string().format(name=self.name, donation=self.donations))
            print(f'Writing: {filename}')

    def output_string(self):
        'Output string for letters'
        format_string = 'Dear {name},\n\nThank you for your generous donation of ' \
                        '${donation}. Please send us more money at your earliest ' \
                        'convenience.'
        return format_string

class DonorHandler:
    def __init__(self):
        self.donors = {}
    def add_donor(self, donor_object):
        self.donors[donor_object.normalized_name] = donor_object

    def thank_you(self, full_name='', donation_amount=int(), **kwargs):
        '''
        If the user (you) selects ‘Send a Thank You’, prompt for a Full Name.
            If the user types a name not in the list, add that name to the data structure and use it.
            If the user types a name in the list, use it.
        Once a name has been selected, prompt for a donation amount.
            Turn the amount into a number – it is OK at this point for the program to crash if \
            someone types a bogus amount.
        Once an amount has been given, add that amount to the donation history of the selected user.
        Finally, use string formatting to compose an email thanking the donor for their generous \
        donation. Print the email to the terminal and return to the original prompt.
        '''
        '''
        Collect, Format and Validate Full name
        '''
        while not full_name:
            full_name_input = input('Please enter full name of the recipient: ').split()
            full_name = self.name_response_valid(full_name_input)
        '''
        Process Full Name
        '''
        ds_names = [name for name in self.donors]

        if full_name in ds_names:
            print(f'Found {full_name} in data_structure')
            while not donation_amount:
                donation_amount = int(input('Please enter a donation amount: '))
            self.donors[full_name].donate(donation_amount)
            print(self.donors[full_name].output_string().format(name=full_name, \
            donation=donation_amount))
        else:
            while not donation_amount:
                donation_amount = int(input('Please enter a donation amount: '))
            self.add_donor(Donor(full_name, donation_amount))
            print(self.donors[full_name].output_string().format(name=full_name, \
            donation=donation_amount))
        return self.donors[full_name].output_string().format(name=full_name, \
        donation=donation_amount)

    def list_donors(self, **kwargs):
        '''
        If the user types ‘list’, show them a list of the donor names and re-prompt
        '''
        for name in self.donors:
            print(name)
        return [name for name in self.donors]

    def create_a_report(self, **kwargs):
        '''
        Creating a Report
        If the user (you) selected “Create a Report”, print a list of your donors, \
        sorted by total historical donation amount.
        '''
        print('Menu: Create a Report')
        top_row = ('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift')
        format_header = '{:<30} | {:<15} | {:<10} | {:<15}\n'
        format_data = '{:<30} $ {:<15.2f}   {:<10} $ {:<15.2f}\n'
        format_string = format_header.format(*top_row)
        for donor in sorted(self.donors.values(), reverse=True):
            name = donor.name
            num_gifts, total_given, avg_gift = donor.metrics()
            format_string += format_data.format(name, total_given, num_gifts, avg_gift)
        print(format_string)
        return format_string

    def send_letters(self, **kwargs):
        '''
        Try to use a dict and the .format() method to do the letter as one big \
        template rather than building up a big string in parts.
        In this version, add a function (and a menu item to invoke it), that goes \
        through all the donors in your donor data structure, generates a thank you \
        letter, and writes it to disk as a text file.
        '''
        for donor in self.donors.values():
            donor.send_letter()
    #Name Validation
    def name_response_valid(self, full_name):
        'Validate and Return Name Input'
        full_name_cap = ''
        try:
            for name in full_name:
                assert name.isalpha()
                full_name_cap += f'{name.capitalize()} '
            full_name = full_name_cap.strip()
        except AssertionError:
            print('Invalid Name. Found non-alphabetic characters')
        else:
            return full_name

#Function to Process Menu Options
def menu(options_dict, **kwargs):
    '''
    The script should prompt the user (you) to choose from a menu of 3 actions: \
    “Send a Thank You”, “Create a Report” or “quit”)
    '''
    options = [option[0:2] for option in enumerate(options_dict.keys(), 1)]
    while True:
        print('Please select a number from the list of the following options: \n')
        for option in options:
            print(option)
        response = menu_response_valid(options)
        response_selection = options[response-1][1]
        options_dict[response_selection](**kwargs)

#Main Menu
def main_menu(**kwargs):
    'Create Main Menu'
    program_options_dict = {'Send a Thank You': thank_you_menu, \
                            'Create a Report': kwargs['donor_handler'].create_a_report, \
                            'Send Letters to Everyone': kwargs['donor_handler'].send_letters, \
                            'quit': quit_menu}
    menu(program_options_dict, **kwargs)

#Thank You Menu
def thank_you_menu(**kwargs):
    '''
    Sending a Thank You
    If the user (you) selects ‘Send a Thank You’, prompt for a Full Name.
    If the user types ‘list’, show them a list of the donor names and re-prompt
    '''
    program_options_ty = {'Send a Thank You': kwargs['donor_handler'].thank_you, \
                        'Action: List': kwargs['donor_handler'].list_donors, \
                        'quit': main_menu}
    menu(program_options_ty, **kwargs)

def quit_menu(**kwargs):
    sys.exit()

#Menu Option Validation
def menu_response_valid(options):
    'Validate Menu Options'
    try:
        response = int(input())
        assert response in [option[0] for option in options]
    except ValueError:
        print('Non-integer value entered. Please try again.')
    except AssertionError:
        print('This number does not exist in the list of options. Please try again.')
    else:
        return response
    #Name Validation

def main():
    'Create Donors'
    jb = Donor('Jeff Bezos', [1, 5, 10])
    bg = Donor('Bill Gates', [10000])
    sj = Donor('Steve Jobs', [20, 50, 100])
    'Create Donors Handle'
    dh = DonorHandler()
    dh.add_donor(jb)
    dh.add_donor(bg)
    dh.add_donor(sj)
    'Call Main Menu'
    main_menu(donor_handler=dh)

if __name__ == '__main__':
    main()
