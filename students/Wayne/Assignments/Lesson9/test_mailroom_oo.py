from mailroom_object import Donor

# test init 

def test_donor_init():
    d = Donor('Dave Grohl')
    assert d.name == 'Dave Grohl'
    assert d.donations == []
    d.add_donations(10000)
    d.add_donations(20000)
    assert d.total_donations == 30000

def test_donors():
    d = Donor('Dave Grohl')
    d.add_donations(30000)

    db = DonorDB()
    db.add_donor(d)
    assert db.get_total_from_donor('Dave Grohl') == 30000

    e = Donor('Steve Dave')
    e.add_donations(40000)
    e.add_donations(50000)

    db.num_donors == 2
