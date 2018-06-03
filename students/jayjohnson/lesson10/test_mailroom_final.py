from mailroom_final import MailRoom, mainloop


def test_MailRoom_init():
    d = MailRoom('BILL', 100.00)
    assert d.name == 'BILL'
    assert d.balance == [100.00]
    #assert print(d) and False
    d.deposit(50.00)
    assert d.balance == [100.00, 50.00]
    d_sum = d.donation_sum()
    assert d.donation_sum() == d_sum

def test_mainloop():
    e = MailRoom('Alex', 1000.00)
    assert e.name == 'Alex'
    assert e.balance == [1000.00]
    e.deposit(500.00)
    assert e.balance == [1000.00, 500.00]

    f = MailRoom('Sam', 30000.00)
    assert f.balance == [30000.00]
    f.deposit(10000.00)
    assert f.balance == [30000.00, 10000.00]

    donor_db = []
    donor_db.append(e)
    donor_db.append(f)

    assert donor_db == donor_db

# def test_report():
#     donor_db = []
#     e = MailRoom('Alex', 1000.00)
#     assert e.name == 'Alex'
#     assert e.balance == [1000.00]
#     e.deposit(500.00)
#     assert e.balance == [1000.00, 500.00]
#
#     f = MailRoom('Sam', 30000.00)
#     assert f.balance == [30000.00]
#     f.deposit(10000.00)
#     assert f.balance == [30000.00, 10000.00]
#
#     donor_db = []
#     donor_db.append(e)
#     donor_db.append(f)
#
#     assert report() and False
