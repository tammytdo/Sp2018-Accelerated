#!/usr/bin/env python3

"""
Jay Johnson
Mailroom Part 4
Add a full suite of unit tests to your mailroom program.

“Full suite” means all the code is tested. In practice,
it’s very hard to test the user interaction, but you can test everything else.
Make sure that there is as little untested code
in the user interaction portion of the program as possible – hardly any logic.
"""
donor_db = [("William Gates, III", [653772.32, 12.17]),
            ("Jeff Bezos", [877.33]),
            ("Paul Allen", [663.23, 43.87, 1.32]),
            ("Mark Zuckerberg", [1663.23, 4300.87, 10432.0]),
            ]

from Mailroom import print_donors, gen_letter, find_donor
from Mailroom import sort_key, print_donor_report, print_letters

def test_print_donors_1():
    assert print_donors() is True

def test_gen_letter_1():
    assert gen_letter("Jeff Bezos") is True

def test_find_donor_1():
    assert find_donor("Jeff Bezos") is True

def test_sort_key_1():
    assert sort_key() is True

def test_print_donor_report_1():
    assert print_donor_report() is True

def test_print_letters():
    assert print_letters() is True
