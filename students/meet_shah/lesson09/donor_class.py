#!/usr/bin/env python3

from functools import reduce

class Donor:

    def __init__(self, name, donations=None):
        self._name = name
        self._donations = [] if donations is None else [donations]


    @property
    def name(self):
        return self._name


    @property
    def donations(self):
        return self._donations


    def add_donations(self, donation):
        self._donations.append(donation)


    @property
    def num_donations(self):
        return len(self._donations)


    @property
    def total_donations(self):
        #return reduce(lambda a, x: a+x, self._donations, 0)
        return sum(self._donations)


    @property
    def average_donations(self):
        return sum(self._donations) * 1.0 / len(self._donations)


    @property
    def information(self):
        return (self._name, self.total_donations, self.num_donations, self.average_donations)

    def __str__(self):
        return "{}: {}".format(self._name, self._donations)


class DonorDB:

    def __init__(self):
        self._donors = {}


    def update_donor(self, donor):
        """
        update_donor update donor's donation, if a donor DNE, this method adds new one to the list
        """
        for donation in donor.donations:
            self._donors.setdefault(donor.name.lower(), Donor(donor.name)).add_donations(donation)


    def get_total_from_donor(self, donor_name):
        return self._donors[donor_name.lower()].total_donations


    def get_donor(self, donor_name):
        return self._donors[donor_name.lower()].information

    @property
    def list_donors(self):
        return [donor.name for _ , donor in self._donors.items()]

    @property
    def num_donors(self):
        return len(self._donors)


    def generate_sorted_report(self):
        return sorted([donor.information for _, donor in self._donors.items()], key=lambda item: item[1], reverse=True)


    def generate_printable_report(self):
        return ['{:20}{:>20}{:>12}{:>14}'.format(*donor_info) for donor_info in self.generate_sorted_report()]


    def __str__(self):
        return str(self._donors.keys())


    def __repr__(self):
        return str(self._donors)
