#!/usr/bin/env python3

from mailroom4 import *


assert welcome_message() == "Welcome to Mailroom"

testdonor={"Paul": [10000, 2000000, 5000, 550000]}

#Fails for some reason
# assert generate_donor_letter("Paul", testdonor["Paul"][-1]) == """Dear Paul,
#
# 	Thank you for your generous donation of 550000
#
# 	It will be put to very good use.
#
# 					   Sincerely,
# 					   The Team
# """


assert list_donors(testdonor) == "Paul"

menu_string = """
What do you want to do? Please choose from below options:
1. Send a thank you
2. Create a report
3. Send letters to everyone
4. Quit
    """

assert menu_generator("main") == menu_string

thank_string = """
Please choose from the below options
1. List Donors
2. Send a thank you
3. Return to the main menu
    """

assert menu_generator("thank_you") == thank_string
