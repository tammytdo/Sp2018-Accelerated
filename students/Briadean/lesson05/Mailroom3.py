#!/usr#!/usr/bin/env python3

import sys


donors_dict = {"Retsuko Rarecho": [100.00, 25.00, 75.00, 200.00],
               "Fenneko Inoue": [10.00, 200.00, 75.00],
               "Haida Kato": [15.00, 15.00, 15.00, 15.00, 15.00],
               "Gori Tsuruta": [25.00, 30.00, 60.00, 90.00],
               "Washimi Koiwasaki": [10.00, 10.00, 10.00, 35.00, 15.00]}


def main_menu_choice():
    """Display main menu and collect user input"""
    user_choice = input("\n1: Send a Thank You\n"
                        "2: Generate a Report\n"
                        "3: Send Letters to Everyone\n"
                        "4: Exit the Mailroom\n"
                        "Please enter your selection from the options above >> ")
    return user_choice


def thank_you_menu():
    """Display Thank You menu and collect user input"""
    user_choice = input("\nPlease enter a donor name, "
                        "'List' to see a list of previous donors, "
                        "or 'Menu' to return to the menu. >> ").title()
    while True:
        if user_choice == "List":
            print()
            print(list_donors())
            # Is there a better way to get back to user_choice = input? Break/return/continue all go back to main menu
            user_choice = input("\nPlease enter a donor name, "
                                "'List' to see a list of previous donors, "
                                "or 'Menu' to return to the menu. >> ").title()
        elif user_choice == "Menu":
            return
        else:
            accept_donation(user_choice)
            return


def list_donors():
    """Make a list of donors that's easily displayable"""
    print("Donor List:")
    # Why is this printing None at the end of the list?
    [print(donor) for donor in donors_dict.keys()]


def accept_donation(name):
    """Accept a new donation. If donor does not already exist, add to dictionary
    and create appropriate data container.
    Params: input = donor name
            returns a thank you letter
    """
    donors_dict.setdefault(name, [])
    donors_dict.setdefault(name, [])
    donation_amt = input("How much are they donating today? >> $ ")
    donors_dict[name].append(float(donation_amt))
    print(generate_thank_you(name, float(donation_amt)))


def generate_thank_you(name, donation):
    """Generates a standardized thank you letter
    Params: input = donor name, most recent donation amounts
            returns a write_letters_disk
    """
    letter = ("\nDear {},\n\n"
              "Thank you for your recent generous donation of ${:,.2f}.\n"
              "It will be put to good use.\n\n"
              "Sincerely,\n"
              "The Resistance Against Giant Flying Meatballs\n".format(name, donation))
    return letter


def write_letters_disk():
    """Writes a thank you letter for each donor in the database to disk"""
    for donor, donation in donors_dict.items():
        letter = generate_thank_you(donor, donation[-1])
        filename = donor + ".txt"
        print("Writing letter for:", donor)
        open(filename, "w").write(letter)


def sort_key(item):
    """Sort function
    Params: input = "item" or "entry" in the dictionary
            returns the "Total Given" column entry
    """
    return item[1]


def generate_report():
    """Build a report of donors"""
    report_lines = []
    for (name, gifts) in donors_dict.items():
        total_given = sum(gifts)
        num_gifts = len(gifts)
        average_gifts = total_given / num_gifts
        report_lines.append((name, total_given, num_gifts, average_gifts))

    report_header = "\n{:20} | {:12} | {:11} | {:12}".format("Donor Name",
                                                             "Total Given",
                                                             "Num Gifts",
                                                             "Average Gifts"
                                                             )

    report_lines.sort(key=sort_key, reverse=True)
    report = []
    report.append(report_header)
    report.append("-" * 55)
    [report.append("{:20}  ${:12,.2f}  {:11}  ${:12,.2f}".format(* line)) for line in report_lines]

    return "\n".join(report)


def display_report():
    """Display the generated report"""
    print(generate_report())


def exit_program():
    menu_dict = {"Y": yes_exit,
                 "N": no_exit}
    while True:
        response = input("\nAre you sure you'd like to exit the program? Y/N>> ").capitalize()
        try:
            menu_dict.get(response)()
        except KeyError:
            print("{} wasn't an available option. Please enter Y or N.".format(repsonse))


def yes_exit():
    print("Goodbye!")
    sys.exit()


def no_exit():
    main_menu_choice()


if __name__ == "__main__":

    menu_dict = {1: thank_you_menu,
                 2: display_report,
                 3: write_letters_disk,
                 4: exit_program}

    print("Welcome to the Mailroom!")
    while True:
        choice = main_menu_choice()
        try:
            choice = int(choice)
        except ValueError:
            print("\nYou must enter an integer to continue! Please try again.")
            continue
        try:
            menu_dict.get(choice)()
        except KeyError:
            print("That wasn't an available option! Please enter {}".format(menu_dict.keys()))
