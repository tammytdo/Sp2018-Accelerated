

"""
simple mailroom program for a non profit
"""

import sys

DONORS = {'Sir Isaac Newton': [100.38, 2, 4, 5000.98],
          'Zach de la Rocha': [1000.76, 5, 235.90, 50.76],
          'Space Ghost': [1, 5, 900000, 76.45]
          }


def thank_you():
    """
    Get into the thank you note generation portion of the program
    """

    options_dict = {"1": add_donation,
                    "2": display_donors,
                    "3": return_to_menu}

    menu_string = """== Send a Thank You ===

    1) Add a new donation (creates new donor profile if a new donor is entered)
    2) Display a list of donors
    3) Back\n"""

    run_loop(options_dict, menu_string)


def input_loop_for_add_donation():

    while True:
        print("Please enter the amount donated:\n")
        input_amount = check_if_number(input(">>"))

        if input_amount:
            return input_amount


def check_if_number(response):

    try:
        donation_amount = float(response)
        return donation_amount
    except ValueError:
        print("invalid input")
        return False


def add_donation():

    print("Please enter the name of the donor:\n")
    donor_name = input(">>")

    donation_amount = input_loop_for_add_donation()

    # while True:
    #     print("Please enter the amount " + donor_name + " donated:\n")
    #     entered_amount = input(">>")
    #     donation_amount = check_if_number(entered_amount)

    add_donation_info(donor_name, donation_amount)


def add_donation_info(name, amount):

    # comp_name_existing = [name.upper() for name in donors]

    DONORS.setdefault(name, []).append(amount)


def display_donors():

    for name in DONORS:
        print(name)


def generate_report():

    report = []
    report_data = []

    header = ("{:<25s} | {:^15s} | {:^10s} | {:15s}".format(
        "Donor Name", "Total Given", "Num Gifts", "Average Gift"))
    divider = "_" * len(header)

    report.append(header)
    report.append(divider)

    for key_name in DONORS:
        name = key_name
        total_given = sum(DONORS[key_name])
        total_count = len(DONORS[key_name])
        avg_given = total_given / total_count
        report_data.append((name, total_given, total_count, avg_given))

    # Sort with respect to "Total Given" value.
    report_data.sort(key=donations, reverse=True)

    # Adding the data into report with formatting
    for data in report_data:
        report.append("{:25s}   ${:14.2f}   {:10d}   ${:11.2f}".format(* data))

    printable_report = "\n".join(report)

    return printable_report


def donations(keys):
    return keys[1]


def print_report():

    print(generate_report())


def letters():

    print("== Send letters to everyone ==")

    for key_name in DONORS:
        file = open("Letter_for_" + key_name + ".txt", "w")

        letter = ("Dear " + key_name + ",\n\n" +
                  "Thank you for your recent donation of $" +
                  "%.2f" % DONORS[key_name][-1] + ".\n\n" +
                  "It will be put to very good use.\n\n" +
                  "Sincerely,\n\n" + "-The Team")

        file.write(letter)

        file.close()


def quit_menu():

    options_dict = {"1": quit, "2": return_to_menu}

    menu_string = """Are you sure you want to quit?
    1) Yes, quit
    2) Back?\n"""

    run_loop(options_dict, menu_string)


def quit():

    sys.exit()


def run_loop(arg_dict, menu_string):

    while True:
        print(menu_string)
        user_input = input(">>")

        if user_input:
            result = selection(arg_dict, user_input)

            if result:
                return


def selection(arg_dict, answer):
    try:
        return arg_dict[answer]()
    except (KeyError):
        return False


def return_to_menu():

    return True


def mainloop():
    """
    main menu loop, where the user can make the choice of
    "Send a Thank You", "Generate a Report", "Send Letters
    to Everyone", or "Quit"
    """

    options_dict = {"1": thank_you, "2": print_report,
                    "3": letters, "4": quit_menu}
    menu_string = """Welcome to Mailroom! 
Please select one of the following options:
    1) Thank You
    2) Report
    3) Send etters to everyone
    4) Quit\n"""

    run_loop(options_dict, menu_string)


if __name__ == "__main__":
    print("...initiating...")
    mainloop()
