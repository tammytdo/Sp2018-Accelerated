#!/usr/bin/env python
import pytest
import os.path
import MailRoomPt3 as MR


def test_One_letter():
    ty_letter = "Donor B"
    DonationVal = 80
    returnval = MR.One_letter(ty_letter, DonationVal)
    assert "Donor B" in returnval
    assert "80.00" in returnval
    #  Passes


def test_All_letters():
    donordict = {'Donor': ['Andrew Wall', 'Jeff Bezos', 'Bill Gates'],
                 'Donation': [100, 260, 420]}
    MR.All_letters(donordict)
    assert os.path.isfile("Andrew Wall.txt")
    assert os.path.isfile("Jeff Bezos.txt")
    assert os.path.isfile("Bill Gates.txt")
    # Passes only after files have been created


def test_report():
    donors = [("Donor A", [10, 20, 30, 40]),
              ("Donor B", [50, 60, 70, 80]),
              ("Donor C", [90, 100, 110, 120])]
    returnval = MR.report(donors)
    assert "420.00" in returnval
    assert "4" in returnval
    assert "105.00" in returnval
    assert 'Donor C' in returnval
    # Passes


def test_thank_you():
    ty_letter = 'Donor A'
    returnval = MR.thank_you()
    assert ty_letter in returnval


'''
This test works as long you go in the code and comment out the
ty_letter = input statement and assign ty_letter 'list' a donor's name that is
actually in the list.  Also I had to add return values after very assignment of
the variable ty_letter.  I could not find a way to get around the input
'IOError' error.  the test_thank_you was diffuclt to construct since I didnt
create any arguments to pass in, I relied on the input within tehe function I
can see why UNIT TESTING is used prior to writing code.  It makes you think
about the entire code on the front end rather than piece meal(which is how I
attempted it).  Although creating a UNIT TEST is difficult, as I worked, I
begain to see the flaws in the code I had written and would design it
differently.
'''
