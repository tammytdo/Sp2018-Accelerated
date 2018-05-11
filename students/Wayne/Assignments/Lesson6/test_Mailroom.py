

"""

Built to test the Mailroom script for bugs

"""
import os

import Mailroom2 as MR

MR.donor_db = MR.find_donor_db()


def test_list_donors_db():
    listing = MR.list_donors()

    assert listing.startswith("Donors:\n")
    assert "Dave Grohl" in listing
    assert "Rivers Cuomo" in listing
    assert len(listing.split('\n')) == 4

def test_search_donor_db():

    donor = MR.search_donor_db("Rivers cuomo")

    assert donor[0] == "Rivers Cuomo"


def test_search_donor_na():

    donor = MR.search_donor_db("Chris Barker")

    assert donor is None


def test_new_donor():
    name = "Will Smith"

    donor = MR.add_new_donor(name)
    donor[1].append(350)
    assert donor[0] == "Will Smith"
    assert donor[1] == [350]
    assert MR.search_donor_db


def test_file_output():

    MR.save_letters_to_disk()

    assert os.path.isfile('Billy_Joe_Armstrong.txt')
    assert os.path.isfile('Dave_Grohl.txt')