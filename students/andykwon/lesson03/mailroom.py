"""
simple mailroom program for a non profit
"""

import sys

donors = [("Sir Isaac Newton", [100.38, 2, 4, 5000.98]),
          ("Zach de la Rocha", [1490.32, 5,19000.33]),
          ("Space Ghost", [1, 5, 90, 76.45]),
          ]

def thank_you():
    """
    Get into the thank you note generation portion of the program
    """
    selection = ""

    print("== Send a Thank You ==\n")
    print("Please enter the name of the person you would like to send a Thank You to."
          "(type 'list' if you would like a list of the donor names\n")

    response_name = input(">>")

    if response_name == "list":
        print(donors)

    # Checking to see if the name is in the donors list
    for item in donors:
        if response_name in item:
            selection = item
            print(selection)

    # If selection did not change from original value, then there is no match
    if selection == "":
        donors.append((response_name, []))

    # Ask for donation amount; add donation amount to associated donation list
    print("Please enter the donation amount:\n")

    response_donation = input(">>")

    for item in donors:
        if response_name in item:
            donors[donors.index(item)][1].append(float(response_donation))


def report():

    print("== Generate a Report ==\n")

    name_length = 0
    given_length = 0
    count_length = 0
    avg_length = 0
    report_list = []

    for i in range(len(donors)):
        name = donors[i][0]
        total_given = sum(donors[i][1])
        total_count = len(donors[i][1])
        avg_given = "%.2f" % (total_given / total_count)

        report_list.extend((name, total_given, total_count, avg_given))

        header = "Donor Name " + " " * (10) + "| Total Given " + "| Num Gifts " + "| Average Gift "
        divider = "_" * len(header)

        # To print the header and dividing line of the table
        if i == 0:
            print(header)
            print(divider)

        # Space calculations to ensure there is appropriate amounts of " " for alignment
        name_space = 22 - len(name)
        total_given_space = 11 - len(str(total_given))
        total_count_space = 12 - len(str(total_count))
        avg_given_space = 12 - len(str(avg_given))

        # Print the results with formatting
        print(name + " " * name_space, end='')
        print("$" + " " * total_given_space + str(total_given), end='')
        print(" " * total_count_space + str(total_count) + "  ", end='')
        print("$" + " " * avg_given_space + str(avg_given))

def quit():
    print("Are you sure you want to quit?\n"
          "1) Yes, quit\n"
          "2) No, don't quit\n")

    response = input(">")

    if response == "1":
        sys.exit()
    elif response == "2":
        return


def mainloop():

    response = ""

    while True:
        print("Welcome to Mailroom")
        print("what do you want to do?")
        print("1) thank you\n"
              "2) report\n"
              "3) quit\n")

        response = input(">>")

        if response not in ("1", "2", "3"):
            print("Not a valid response")
        elif response == "1":
            thank_you()
            continue
        elif response == "2":
            report()
            continue
        elif response == "3":
            quit()
            continue


if __name__ == "__main__":
    mainloop()
