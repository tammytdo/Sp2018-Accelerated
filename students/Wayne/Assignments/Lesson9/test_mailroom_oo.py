from mailroom_oo import Donor
from mailroom_oo import DonorData
from mailroom_oo import testdb
import os

# test init 

def test_donor_init():
    d = Donor('Dave Grohl')
    assert d.name == 'Dave Grohl'
    assert d.donations == []
    d.add_donation(10000)
    d.add_donation(20000)
    assert d.total_donations == 30000


def test_file_output():

    DonorData.save_letters_to_disk()
    DonorData.save_letters_to_disk()

    assert os.path.isfile('Billy_Joe_Armstrong.txt')
    assert os.path.isfile('Dave_Grohl.txt')

def test_donors():
    d = Donor('Steve Dave')
    d.add_donation(30000)

    DonorData.add_donor(d)
    assert testdb.get_total_from_donor('Steve Dave') == 30000

    e = Donor('Steve Dave')
    e.add_donation(40000)
    e.add_donation(50000)

    db.num_donors == 2
