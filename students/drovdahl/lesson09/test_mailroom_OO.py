#! /usr/local/bin/python3

from mailroom_OO import *
from pathlib import Path


def test_initiateDB():
    initiate_db()


def test_donor_init():
    d = Donor('Test Monkey1')
    assert d.name == 'Test Monkey1'
    assert d.donations == []
    e = Donor('Test Monkey2', donations=[10, 20])
    assert e.name == 'Test Monkey2'
    assert e.donations == [10, 20]


def test_donation_add():
    d = Donor('Test Monkey1')
    d.add_donation(10000)
    d.add_donation(20000)
    assert d.total_donations == 30000


def test_db_setup():
    db = DonorDB()
    db.add_donor(Donor('Test Monkey1', donations=[111, 222]))
#    print(db.get_donors_list())
    assert 'Test Monkey1' in db.get_donors_list()
#    print(db.get_all())
    assert '$111, $222' in db.get_all()


def test_generate_thankyou_letter():
    donor = 'Test Monkey20'
    donor_donation = 1000
    assert('Dear Test Monkey20' and '400.00 kitten') in\
        thankyou_letter(donor, donor_donation)


def test_dir_generation():
    letters_to_all(TEST=True)
    my_dir = Path('letters')
    assert my_dir.is_dir() is True
