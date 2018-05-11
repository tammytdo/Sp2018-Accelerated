from mailroom2_working import Donor

def test_donor _init():
    d = Donor("William Gates III")
    assert d.name == "William Gates III"
    assert d.donations == []
    d.add_donation(10000)
    d.add_donation(20000)
    assert d.total_donations == 30000
    assert print(d) and False

def test_donors():
    d = Donor("Paul Alen")
    d.add_donation(30000)

    db = DonorDB()
    db.add_donor(d)

    db = DonorDB()
    db.add_donor(d)
    assert db.get_total_from_donor("Paul Allen") == 30000

    e = Donor("Jeff Bezos")
    e.add_donation(40000)
    asser db.num_donors == 2
    assert print(db) and False