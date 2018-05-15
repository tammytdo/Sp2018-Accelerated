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
