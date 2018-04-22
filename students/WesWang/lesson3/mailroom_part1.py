#=========================================================================================
#Name: Mailroom
#Author: Wesley Wang
#Date: 4/18/2018
#=========================================================================================

"""
Mailroom Part1
"""
import sys

donors = [["Donor A", 140000, 2],
          ["Donor B", 1000, 1],
          ["Donor C", 3000, 3],
          ["Donor D", 20000, 4]]

def thank_letter(donor, amount):
  print("-"*80)
  print(f"Dear {donor},\n\n\tWe have received you donation of ${amount:,.2f}. We greatly appreciate your generous contribution. This donation is meaningful and crucial to our organization's misson.\n\n\nSincerely,\n\nWesley Wang\n")
  print("-"*80)

def thank_you():
    # Ask for user input
    response = input("Please enter donor's full name, or type 'list' to check all donors: ").title()
    if response.lower() == "list":
      print("-"*20 + "\nList of Donors:\n" + "-"*20)
      for donor in donors:
        print(donor[0])
      print("-"*20)
      thank_you()
    amount = int(input("Please enter donation amount for " + response + ":"))
    for donor in donors:
      if response.lower() == donor[0].lower():
        donor[1] += amount
        donor[2] += 1
        thank_letter(donor[0], amount)
        print("Return to main menu!!")
        mainloop()
    donors.append([response, amount, 1])
    thank_letter(response, amount)
    mainloop()


def report():
  #header = "Donor Name" + " "*30 + "| Total Given | Num Gifts | Average Gifts |"
  header = "{:30}| {:15}| {:10}| {:20}".format("Donor Name","Total Given", "Num Gifts","Average Gifts")
  print("-"*75)
  print(header)
  print("-"*75)

  for donor in donors:
    if len(donor[0]) > 30:
      print("Error: Donor name exceeds length limit! Please verify " + donor[0] + "'s information")
    elif len(str(donor[1])) > 9:
      print("Error: Donated amount exceeds limit (6 digits)! Please verify " + donor[0] + "'s information!")
    elif len(str(donor[2])) > 10:
      print("Error: Donation number exceeds limit! Please verify " + donor[0] + "'s information!")
    else:
      print(f"{donor[0]:30}${donor[1]:>15,.2f}{donor[2]:>13}{donor[1]/donor[2]:>15,.2f}")
  print("-"*75)

def quit():
    print("You have successfully quit Mailroom")
    sys.exit()

def mainloop():
    print("Welcome to the Mailroom")

    response = ""
    while response != "3":
        print("What do you want to do?")
        response = input("[1] Thank you\n[2] Report\n[3] Quit\n")
        print(response, " was chosen")

        if response not in ("1","2","3"):
            print("Not a Valid Response --- Type 1,2,3")
        elif response == "1":
            thank_you()
        elif response == "2":
            report()
        else:
            quit()


if __name__ == "__main__":
    mainloop()
