"""
simple mailroom program for a non profit
"""

import sys

donors = [("Donor A", [1, 2, 4, 5]),
          ("Donor B", [14, 5]),
          ("Donor C", [1, 5, 90]),
          ]

print(donors)

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
           donors[donors.index(item)][1].append(response_donation)


    print(donors)


def report():
    print("== Generate a Report ==\n")

    for i in range (len(donors)):
        name = donor[i][0]
        total_given = sum(donor[i][1])
        total_count = len(donors[i][1])
        avg_given = total_given / total_count




def quit():
    print("Are you sure you want to quit?\n"
          "1) Yes, quit"
          "2) No, don't quit")

    response = input(">")

    if response == "1":
        sys.exit()
    elif response == "2":
        mainloop()


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

