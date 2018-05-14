#!/usr/bin/env python3

from donor_class import Donor
from donor_class import DonorDB

donors = {"William Gates, III": [10000, 2000000, 5000, 550000],
          "Mark Zuckerberg": [10, 100, 25, 100],
          "Jeff Bezos": [50,  10, 15, 100],
        }

def test_donor_init():

    d = Donor('William Gates III')
    assert d.name == 'William Gates III'

    d.add_donations(10000)
    d.add_donations(20000)

    assert d.num_donations == 2
    assert d.total_donations == 30000
    #assert d.total_donations() == 30000
    #assert d.num_donations()


def test_donor_db():

    db=DonorDB()
    mydonor = Donor('William Gates')


if __name__ == "__main__":
    test_donor_init()
    test_donor_db()
