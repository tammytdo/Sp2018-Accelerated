#!/usr/bin/env python


def test_data():

    donors = ["John Smith", "Ringo Eclipse", "Burt Syran", "Lance J. Johnson",
              "Orel Winfrey"]
    donations = [[25, 25], [25, 25, 25, 25], [50, 50, 50, 150], [25, 25, 50, 25], [500]]
    return dict(zip(donors, donations))


def pack(don):
    n, don = don
    total = sum(don)
    number = len(don)
    return (n, total, number, (total / number))

def create_donors_report(DONORS):
    # donor_report = [pack(don) for don in DONORS.items()]
    # for n, don in DONORS.items():
    #     total = sum(don)
    #     number = len(don)
    #     donor_report.append((n, total, number, total / number))
        # name.append(n)
        # total.append(sum(don))
        # number.append(len(don))
        # avg.append(total[-1] / number[-1])
    
    # def key(y):
    #     return y[1]
    # donors_report = sorted(zip(name, total, number, avg),
    #                      key=lambda y: y[1], reverse=True)
    # donor_report.sort(key=lambda y: y[1], reverse=True)
    donor_report = sorted([pack(don) for don in DONORS.items()], key=lambda y: y[1], reverse=True)
    return donor_report

