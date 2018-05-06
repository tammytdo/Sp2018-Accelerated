#!/usr/bin/env python

"""
Test code for Mailroom Assignment
"""
import pytest
import mailroom_4 as m
import os

# Create a data object to store donor information
test_donors = {
    'Jeff Bezos': [50, 100, 56],
    'Mark Zuckerberg': [45, 105, 349, 101, 78],
    'Paul Allen': [10, 50, 400, 400],
    'Elon Musk': [16, 68, 170, 425],
    'Richard Branson': [25, 90, 124, 300]
    }

def test_gen_letter():
    # test_donor = next(iter(test_donors))
    # last_donation = test_donors[test_donor][-1]
    # test = (test_donor, last_donation)
    test = ('Jeff Bezos', 56)
    assert m.gen_letter(*test) == 'Dear Jeff Bezos,\n\nWe greatly appreciate your generous donation of $56.00.\n\nThank you,\nThe Team'
    assert 'Jeff Bezos' in m.gen_letter(*test)
    assert '$56.00' in m.gen_letter(*test)

def test_filename():
    assert m.filename('Jeff Bezos') == 'Jeff_Bezos.txt'

def test_write_letters_to_disk():
    """
    Spot check if some of the files exist and that they are not empty
    """
    m.write_letters_to_disk(test_donors)
    assert os.path.isfile('Jeff_Bezos.txt')
    assert os.path.isfile('Richard_Branson.txt')
    with open('Jeff_Bezos.txt') as f:
        size1 = len(f.read())
    assert size1 > 0
    with open('Richard_Branson.txt') as f:
        size2 = len(f.read())
    assert size2 > 0

def test_add_donation():
    m.add_donation('Elmer Fudd', 14, test_donors)
    assert 'Elmer Fudd' in test_donors
    assert test_donors['Elmer Fudd'][-1] == 14

def test_donor_list():
    donors = m.donor_list(test_donors)
    assert donors.startswith('Jeff Bezos')
    assert donors.endswith('Elmer Fudd\n')

def test_avg_donations():
    test_donations = ['Elmer Fudd', [50, 100, 50, 40]]
    assert m.avg_donations(test_donations) == 60

def test_sum_donations():
    test_donations = ['Elmer Fudd', [50, 100, 50, 40]]
    assert m.sum_donations(test_donations) == 240

def test_report_data():
    test_str = m.report_data(test_donors)
    assert test_str.startswith('Paul Allen')
    assert test_str.endswith('$14.00\n')