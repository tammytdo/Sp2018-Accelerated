

"""
simple mailroom program for a non profit
"""

import sys

donors = {'Sir Isaac Newton': [100.38, 2, 4, 5000.98],
          'Zach de la Rocha': [1000.76, 5, 235.90, 50.76],
          'Space Ghost': [1, 5, 900000, 76.45]
          }


def thank_you():
    """
    Get into the thank you note generation portion of the program
    """
    selection = ""

    print("== Send a Thank You ==\n\n")
    print("1) Add a new donation (creates new donor profile if a new name is entered.\n"
          "2) Display a list of the donors.\n"
          "3) Quit\n")

    response = input(">>")

    if response == "1":
        response_name = input(">>")

        response_donation = input(">>")

        if response_name in donors:
            donors[response_name].append(response_donation)
        else:
            donors[response_name] = []
            donors[response_name].append(float(response_donation))

    elif response == "2":
        print(donors)

    elif response == "3":
        return

    # Can the above if/else be replaced with setdefault?? look into it...


def donations(keys):
    return keys[1]


def report():
    """
    prints a report of the donors and their contributions
    """
    print("== Generate a Report ==\n")

    report = []
    report_data = []

    header = ("{:<25s} | {:^15s} | {:^10s} | {:15s}".format(
        "Donor Name", "Total Given", "Num Gifts", "Average Gift"))
    divider = "_" * len(header)

    report.append(header)
    report.append(divider)

    for key_name in donors:
        name = key_name
        total_given = sum(donors[key_name])
        total_count = len(donors[key_name])
        avg_given = total_given / total_count
        report_data.append((name, total_given, total_count, avg_given))

    # Sort with respect to "Total Given" value.
    report_data.sort(key=donations, reverse=True)

    # Adding the data into report with formatting
    for data in report_data:
        report.append("{:25s}   ${:14.2f}   {:10d}   ${:11.2f}".format(* data))

    print("\n".join(report))
    return "\n".join(report)


def letters():

    print("== Send letters to everyone ==")

    for key_name in donors:
        file = open("Letter_for_" + key_name + ".txt", "w")

        letter = ("Dear " + key_name + ",\n\n" +
                  "Thank you for your recent donation of $" +
                  "%.2f" % donors[key_name][-1] + ".\n\n" +
                  "It will be put to very good use.\n\n" +
                  "Sincerely,\n\n" + "-The Team")

        file.write(letter)

        file.close()


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
              "3) Send letters to everyone\n"
              "4) quit\n")

        response = input(">>")

        if response not in ("1", "2", "3", "4"):
            print("Not a valid response")
        elif response == "1":
            thank_you()
            continue
        elif response == "2":
            report()
            continue
        elif response == "3":
            letters()
            continue
        elif response == "4":
            quit()
            continue


if __name__ == "__main__":
    mainloop()
