#!/usr/bin/env python



#       Implementing cleaver student soluton for Dict-Switch **Brilliant!**
#       Source: https://github.com/mathewcmartin/Sp2018-Accelerated/blob/master
#       /solutions/Lesson05/mailroom_dict_switch.py
#

import sys

donors = ["John Smith", "Ringo Eclipse", "Burt Syran", "Lance J. Johnson",
          "Orel Winfrey"]
donations = [[25, 25], [25, 25, 25, 25], [50, 50, 50, 150], [25, 25, 50, 25], [500]]

# Global variable for donors and dues paid

DONORS = dict(zip(donors, donations))
del donors
del donations

def quit_func():
    sys.exit()

def return_to_menu():
    """ returns true to exit out of subloop: from solutions"""
    return True


def create_donors_report():
    [name, total, number, avg] = [[], [], [], []]
    for x in DONORS:
        name.append(x)
        total.append(sum(DONORS[x]))
        number.append(len(DONORS[x]))
        avg.append(total[-1] / number[-1])
    donors_report = list(zip(name, total, number, avg))
    donors_report = sorted(
            donors_report, key=lambda y: int(y[1]), reverse=True)
    return donors_report

def config_donors_report():
    print_report(create_donors_report())

def report_display_config():
    """Configures display of donors_report in terminal"""
    headers = ('Donor Name', 'Total donation', '# of donations', 'Avg donation')
    data = '|'.join(["{:<40}", "{:<12}", "{:<10}", "{:<12}"])
    width = len(data.format(*headers))
    head = (data.format(*headers)) + '\n'
    head = head + (width * "-") + '\n'
    return head

def report_body_config(list_data):
    """Configures display of donors_report body"""
    body = ""
    data = ''.join(["{:<40}", "${:^12.2f}", "{:^12d}", "${:^12.2f}"])
    for i in range(len(list_data)):
        entry = list_data[i]
        body = body + data.format(*entry) + '\n'
    return body

def print_report(list_data):
    print(report_display_config())
    print(report_body_config(list_data))


# Donations and thank you functions


def collect_donor_input():
    """ Get name and donation amount to add to DONORS"""
    fullname = input("Enter a donor name (new or existing):\n")
    fullname = remove_quotes(fullname)
    amount = float(input("Donation amount: "))
    return (fullname, amount)

def retrieve_donations(fullname):
    """ if donors exists, return donations, otherwise return None"""
    if fullname in DONORS:
        return DONORS[fullname]

def add_donation(fullname, amount):
    DONORS.setdefault(fullname, []).append(amount)

def update_donors():
    """
    Add new donation to donors: if new donor, add to DONOR.
    Print a thank you note for the donation.
    """
    (fullname, amount) = collect_donor_input()
    add_donation(fullname, amount)
    print(create_letter(fullname))

def list_donors():
    print(make_donor_list())

def make_donor_list():
    o_data = ""
    return ("Donor Names:" + "".join([o_data + '\n' + x for x in DONORS]))

def create_letter(donor_name):
    """Create a thank you note to the donor and return the string"""
    data = "Thanks, {} for the donation, it is well received. Your gift of ${} is vital in our efforts."
    return data.format(donor_name, DONORS[donor_name][-1])

# Input functions

def remove_quotes(a_string):
    a_string.replace('"', '')
    return a_string

def select_action(arg_dict, ans):
    try:
        return arg_dict[ans]()
    except (KeyError):
        return False

# Mainloop functions

def send_ltrs():
    for donor in DONORS:
        outfile = donor.replace(" ", "_") + '.txt'
        with open(outfile, 'w') as f:
            f.write(create_letter(donor))
    print("Donor letter files created.")

def run_interactive_loop(arg_dict, prompt_string):
    """ Brilliant solution provided by prior CEB Student. Kudos not mine!!!"""
    while True:
        ans = input(prompt_string)
        if ans:
            result = select_action(arg_dict, ans)
            if result:
                return

def thank_you_loop():
    """ Primary loop to update and thank DONORS
    update DONORS, print donor names, or return to main menu
    """
    arg_dict = {"1": update_donors, "2": list_donors, "3": return_to_menu}
    prompt_string = """To send a thank you, select one:\n
    (1) Update donor and send thank-you\n
    (2) List all existing DONORS\n
    (3) Return to main menu\n >"""
    run_interactive_loop(arg_dict, prompt_string)


def print_report_loop():
    """ Primary reporting loop
    "generate report table" or "return to main menu"
    """
    arg_dict = {"1": config_donors_report, "2": return_to_menu}
    prompt_string = """Select one:\n
    (1) Generate a summary report\n
    (2) Return to the main menu\n"""
    run_interactive_loop(arg_dict, prompt_string)


def mainloop():
    """Main menu loop"""
    arg_dict = {"1": thank_you_loop, "2": print_report_loop,
                "3": send_ltrs, "4": quit_func}
    prompt_string ="""Select from one of the options: \n
    (1) Send Thank You letter\n
    (2) Create report\n
    (3) Send letters to all donors\n
    (4) Quit\n"""
    run_interactive_loop(arg_dict, prompt_string)

if __name__ == "__main__":
    mainloop()
