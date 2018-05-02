#!/usr/bin/env python


def test_data():

    donors = ["John Smith", "Ringo Eclipse", "Burt Syran", "Lance J. Johnson",
              "Orel Winfrey"]
    donations = [[25, 25], [25, 25, 25, 25], [50, 50, 50, 150], [25, 25, 50, 25], [500]]
    return dict(zip(donors, donations))

# creates a list and unpacks it
# looping through the donors and computing name, total, number etc
# donor is dictionary and x is looking at the name key
# changed variable to n for styling
# zip returns an iterable of tuples
# removed the list
# lambda allows you to write little key functons into your cold
# a function that is passed an item will return what you want to
# sort by
# key function returns index 1




def create_donors_report(DONORS):
    [name, total, number, avg] = [[], [], [], []]
    for x in DONORS:
        name.append(x)
        total.append(sum(DONORS[x]))
        number.append(len(DONORS[x]))
        avg.append(total[-1] / number[-1])
    donors_report = list(zip(name, total, number, avg))
    donors_report = sorted(donors_report,
                           key=lambda y: int(y[1]), reverse=True)
    return donors_report

#after

def create_donors_report(DONORS):
    [name, total, number, avg] = [], [], [], []
    donors_report = []
    for n, don in DONORS.items():
        donor_report.append(n,
                          sum(don),
                          len(don)
                          (total[-1] / number[-1])
                          )
        name.append(n)
        total.append(*sum(don))
        number.append(len(don))
        avg.append(total[-1] / number[-1])

    def key(y):
        return y[1]
    donor_report = sorted(zip(name, total, number, avg),
                           key=key, reverse=True)
    return donors_report