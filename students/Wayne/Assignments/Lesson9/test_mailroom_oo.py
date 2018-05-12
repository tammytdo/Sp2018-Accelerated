from mailroom_oo import Donor

# test init 

def test_donor_init():
    d = Donor('Paul Allen')
    assert d.name == 'Paul Allen'
    assert d.donations == []
    d.add_donations(10000)
    d.add_donations(20000)
    assert d.total_donations == 30000

def test_donors():
    d = Donor('Paul Allen')
    d.add_donations(30000)

    db = DonorDB()
    db.add_donor(d)
    assert db.get_total_from_donor('Paul Allen') == 30000

    e = Donor('Jeff Bezos')
    e.add_donations(40000)
    e.add_donations(50000)

    db.num_donors == 2

    