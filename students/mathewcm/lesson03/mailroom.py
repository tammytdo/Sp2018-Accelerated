#!/usr/bin/env python


"""
simple mailroom program for a non profit
"""



"""
original list of donors
donors = [("Donor A", [50, 100, 25, 100]),
                ("Donor B"), [50, 25]),
                ("Donor C"), [50, 100, 100]),
                ]

"""
#
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

def thank_you():
    print("This is a thank_you function")


def report():
    print("This is a report function")

def quit():
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
    


    













def mainloop():
    print("Welcome to Mailroom")

    response = ""
    while True:
        print("What do you want to do?")
        print("1) thank you\n"
                "2) report\n"
                "3) quit\n")
        response = input(">> ")

        if response not in ('1', '2', '3'):
            print("Not a Valid response -- type 1,2,3")
            continue
        elif response == "1":
            thank_you()
            continue
        elif response == "2":
            report()
            continue
        elif response == "3":
            quit()

if __name__ == "__main__":
    mainloop()
