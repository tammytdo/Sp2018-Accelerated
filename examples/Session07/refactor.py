#!/usr/bin/env python


def test_data():

    donors = ["John Smith", "Ringo Eclipse", "Burt Syran", "Lance J. Johnson",
              "Orel Winfrey"]
    donations = [[25, 25], [25, 25, 25, 25], [50, 50, 50, 150], [25, 25, 50, 25], [500]]
    return dict(zip(donors, donations))


def create_donors_report(DONORS):
    name, total, number, avg = [], [], [], []
    #donor_info = []
    for n, don in DONORS.items():
        name.append(n)
        total.append(sum(don))
        number.append(len(don))
        avg.append(total[-1] / number[-1])
    donors_report = list(zip(name, total, number, avg))
    donors_report = sorted(donors_report,
                           key=lambda y: int(y[1]), reverse=True)
    return donors_report


def pack()
