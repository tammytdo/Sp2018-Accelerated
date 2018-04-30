#! /usr/local/bin/python3

'''
Test script for mailroom_4
'''
import mailroom_4 as mailroom
from pathlib import Path
import datetime

donors_dict = {'Iron Man': [100000, 50000, 1000],
               'Thor': [50, 25, 100],
               'Hulk': [500],
               'Captain America': [30, 40],
               'Nick Fury': [100000, 545, 1000],
               'Hawkeye': [75, 50, 20],
               'Black Panther': [1000, 900, 50],
               'War Machine': [10, 10]}


def test_add_and_remove_new_donor():
    mailroom.donors_dict = donors_dict
    donor = 'Test Monkey'
    donor_donation = 123456789.10
    mailroom.add_donation(donor, donor_donation)
    assert mailroom.retrieve_donation(donor) == [donor_donation]
    assert mailroom.delete_donor(donor) == [donor_donation]


def test_retrieve_donation():
    mailroom.donors_dict = donors_dict
    donor = 'Test Monkey'
    assert mailroom.retrieve_donation(donor) is None


def test_retrieve_donation2():
    mailroom.donors_dict = donors_dict
    donor = 'War Machine'
    assert mailroom.retrieve_donation(donor) == [10, 10]


def test_add_donation_to_existing_donor():
    mailroom.donors_dict = donors_dict
    donor = 'War Machine'
    donor_donation = 10
    mailroom.add_donation(donor, donor_donation)
    assert mailroom.retrieve_donation(donor) == [10, 10, 10]


def test_generate_thankyou_letter():
    mailroom.donors_dict = donors_dict
    donor = 'Test Monkey'
    donor_donation = 1000
    assert('Dear Test Monkey' and '400.00 kitten') in\
        mailroom.thankyou_letter(donor, donor_donation)


def test_dir_generation():
    mailroom.donors_dict = donors_dict
    mailroom.letters_to_all(TEST=True)
    my_dir = Path('letters')
    assert my_dir.is_dir() is True


def test_file_generation():
    mailroom.donors_dict = donors_dict
    mailroom.letters_to_all(TEST=True)
    dt_format = '.%m-%d-%Y'
    for donor in donors_dict:
        my_file = Path('letters/' + donor +
                       datetime.datetime.now().strftime(dt_format) + '.txt')
        assert my_file.is_file() is True
