#!/usr/bin/env python3

"""
test code for mailroom4
"""

import mailroom4 as mr

def test_donors_name_list():
    donors = mr.donors_name_list()
    print(donors)
    assert 'William Gates III' in donors
    assert 'Jeff Bezos' in donors
    assert len(donors) == len(mr.old_datas)


def test_datas():
    assert len(mr.datas) == len(mr.old_datas)


def test_find_donor():
    mr.datas = {'William Gates III': [ 653784.39, 0],
                'Mark Zuckerberg': [16396.10, 0, 0],
                'Jeff Bezos': [877.33],
                'Paul Allen': [708.42, 0, 0],
                'Ruohan': [500]}
    donor = 'Ruohan'
    amount = 500
    mr_data = mr.find_donor(donor)
    assert mr_data == mr.data


def test_letter():
    donor = "Ruohan"
    amount = 500
    mr.letter(donor, amount)
    assert mr.find_donor(donor)[donor] == amount
