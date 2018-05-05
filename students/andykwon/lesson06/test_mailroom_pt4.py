#!/usr/bin3/env python3

import mailroom_pt4 as mailroom
import os.path


def test_add_donation_info():
    """
    Testing to see if a new name creates a new entry in DONORS.in
    Also test to see if associated value is added. 
    """
    mailroom.DONORS = {'Sir Isaac Newton': [100.38, 2, 4, 5000.98],
                       'Zach de la Rocha': [1000.76, 5, 235.90, 50.76],
                       'Space Ghost': [1, 5, 900000, 76.45]
                       }
    name = "andy"
    amount = 1000000.0
    mailroom.add_donation_info(name, amount)
    print(mailroom.DONORS)
    assert "andy" in mailroom.DONORS
    assert amount in mailroom.DONORS[name]


def test_add_donation_info_2():
    """
    Test to see if the the name already exists, the donation amount is added
    to the proper donor.
    """
    mailroom.DONORS = {'Sir Isaac Newton': [100.38, 2, 4, 5000.98],
                       'Zach de la Rocha': [1000.76, 5, 235.90, 50.76],
                       'Space Ghost': [1, 5, 900000, 76.45]
                       }
    name = "Sir Isaac Netwon"
    amount = 1000000.0
    mailroom.add_donation_info(name, amount)
    print(mailroom.DONORS)
    assert amount in mailroom.DONORS[name]


def test_generate_report():
    """
    Test to see if the proper values are contained in the list generated from 
    generate report. The values are the sum, average and counts.
    """
    mailroom.DONORS = {'Sir Isaac Newton': [100.38, 2, 4, 5000.98],
                       'Zach de la Rocha': [1000.76, 5, 235.90, 50.76],
                       'Space Ghost': [1, 5, 900000, 76.45]
                       }
    result = mailroom.generate_report()
    assert "900082.45" in result
    assert "4" in result
    assert "225020.61" in result


def test_selection_sad():
    """
    Test to see if invalid input yields False
    """
    options_dict = {"1": thank_you, "2": mailroom.print_report}
    answer = "6"
    assert mailroom.selection(options_dict, answer) is False


def test_selection_happy():
    """
    Test to see if invalid input yields False
    """
    options_dict = {"1": thank_you, "2": mailroom.print_report}
    answer = "1"
    assert mailroom.selection(options_dict, answer) == "happy"


def thank_you():
    """
    for test_selection_happy() 
    """
    return "happy"


def test_check_if_number_sad():
    """
    Test to see if entering a non-numerical value returns False
    """
    user_input = "not a number"
    assert mailroom.check_if_number(user_input) == False


def test_check_if_number_happy():
    """
    Test to see if entering a numerical value returns a float of that number
    """
    user_input = "100.00"
    assert mailroom.check_if_number(user_input) == float(user_input)


def test_return_to_menu():
    result = mailroom.return_to_menu()
    assert result is True
