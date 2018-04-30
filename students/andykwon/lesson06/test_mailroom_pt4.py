#!/usr/bin3/env python3

import mailroom_pt4 as mailroom
import os.path


def test_add_donation_info():
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
    mailroom.DONORS = {'Sir Isaac Newton': [100.38, 2, 4, 5000.98],
              'Zach de la Rocha': [1000.76, 5, 235.90, 50.76],
              'Space Ghost': [1, 5, 900000, 76.45]
              }
    name = "Sir Isaac Netwon"
    amount = 1000000.0
    mailroom.add_donation_info(name, amount)
    print(mailroom.DONORS)
    assert amount in mailroom.DONORS[name]