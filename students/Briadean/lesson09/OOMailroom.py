import sys

donors_dict = {"Retsuko Rarecho": [100.00, 25.00, 75.00, 200.00],
               "Fenneko Inoue": [10.00, 200.00, 75.00],
               "Haida Kato": [15.00, 15.00, 15.00, 15.00, 15.00],
               "Gori Tsuruta": [25.00, 30.00, 60.00, 90.00],
               "Washimi Koiwasaki": [10.00, 10.00, 10.00, 35.00, 15.00]}


class Donor:
    def __init__(self, name, donations=None):
        self.name = name.title()
        self.donations = [] if donations is None else donations

    def add_donation(self, donation):
        self.donations.append(donation)


class DonorDB:
    def __init__(self):
        self._donors = {}

    def add_donor(self, donor):
        #  fixme add a check to make sure im not overwriting anything already in the db
        self._donors[donor.name] = donor

    def print_donors(self):
        print("Donor List:")
        for donor in self._donors:
            print(donor)

    def generate_report(self):
        """Build a report of donors"""
        report_lines = []
        for donor in self._donors.values():
            total_given = sum(donor.donations)
            num_gifts = len(donor.donations)
            average_gifts = total_given / num_gifts
            report_lines.append((donor.name, total_given, num_gifts, average_gifts))

        report_header = "\n{:20} | {:12} | {:11} | {:12}".format("Donor Name",
                                                                 "Total Given",
                                                                 "Num Gifts",
                                                                 "Average Gifts"
                                                                 )

        report_lines.sort(key=self._sort_key, reverse=True)
        report = []
        report.append(report_header)
        report.append("-" * 55)
        [report.append("{:20}  ${:12,.2f}  {:11}  ${:12,.2f}".format(*line)) for line in report_lines]

        print("\n".join(report))

    @staticmethod
    def _sort_key(item):
        """Sort function
        Params: input = "item" or "entry" in the dictionary
                returns the "Total Given" column entry
        """
        return item[1]

    def generate_thank_you(self, name, donation):
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

    def write_letters_disk(self):
        """Writes a thank you letter for each donor in the database to disk"""
        for donor, donation in donors_dict.items():
            letter = self.generate_thank_you(donor, donation[-1])
            filename = donor + ".txt"
            print("Writing letter for:", donor)
            open(filename, "w").write(letter)

    def accept_donation(self, donor_name):
        """Accept a new donation.
        Params: input = donor name
        """
        donation_amt = float(input("\nHow much are they donating? >>$ "))
        try:
            self._donors[donor_name].add_donation(donation_amt)
        except KeyError:
            donor = Donor(name=donor_name, donations=[donation_amt])
            self.add_donor(donor)


def seed_db(db):
    for name, donation in donors_dict.items():
        donor = Donor(name=name, donations=donation)
        db.add_donor(donor)


def main():
    db = DonorDB()
    seed_db(db)

    menu_dict = {1: thank_you_menu,
                 2: db.write_letters_disk,
                 3: db.generate_report,
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
            if choice == 1:
                menu_dict.get(choice)(db)
            else:
                menu_dict.get(choice)()
        except KeyError:
            print("That wasn't an available option! Please enter {}".format(menu_dict.keys()))


def main_menu_choice():
    """Display main menu and collect user input"""
    user_choice = input("\n1: Enter a New Donation\n"
                        "2: Generate Thank You Letters for all Donors\n"
                        "3: Generate a Report\n"
                        "4: Exit the Mailroom\n"
                        "\nPlease enter your selection from the options above >> ")
    return user_choice


def thank_you_menu(db):
    """Display Thank You menu and collect user input"""
    user_choice = input("\nPlease enter a donor name, "
                        "'List' to see a list of previous donors, "
                        "or 'Menu' to return to the menu. >> ").title()
    while True:
        if user_choice == "List":
            db.print_donors()
            user_choice = input("\nPlease enter a donor name, "
                                "'List' to see a list of previous donors, "
                                "or 'Menu' to return to the menu. >> ").title()
        elif user_choice == "Menu":
            return
        else:
            db.accept_donation(user_choice)
            return


def exit_program():
    menu_dict = {"Y": yes_exit,
                 "N": no_exit}
    while True:
        response = input("\nAre you sure you'd like to exit the program? Y/N>> ").capitalize()
        try:
            menu_dict.get(response)()
        except KeyError:
            print("{} wasn't an available option. Please enter Y or N.".format(response))


def yes_exit():
    print("Goodbye!")
    sys.exit()


def no_exit():
    main_menu_choice()


if __name__ == "__main__":

    main()
