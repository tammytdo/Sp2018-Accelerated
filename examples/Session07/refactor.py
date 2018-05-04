#!/usr/bin/env python


def test_data():

    donors = ["John Smith", "Ringo Eclipse", "Burt Syran", "Lance J. Johnson",
              "Orel Winfrey"]
    donations = [[25, 25], [25, 25, 25, 25], [50, 50, 50, 150], [25, 25, 50, 25], [500]]
    return dict(zip(donors, donations))


def pack(don):
    n, don = don
    total = sum(don)
    return (n, total, len(don), (total / len(don)))


def create_donors_report(DONORS):
    donor_report = sorted([pack(don) for don in DONORS.items()],
                          key=lambda y: y[1], reverse=True)
    return donor_report

