

"""

Built to test the Mailroom script for bugs

"""


import Mailroom2 as MR


def test_accept_donation():
    amount = 1400
    MR.accept_donation( amount)
    assert MR.donor_db == {[1400]}