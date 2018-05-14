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


    def add_donation(self, donation):
        self._donations.append(donation)


    def add_donations(self, mylist):
        self._donations += mylist

    @property
    def num_donations(self):
        return len(self._donations)


    @property
    def total_donations(self):
        return reduce(lambda a, x: a+x, self._donations, 0)


    @property
    def average_donations(self):
        return sum(self._donations) * 1.0 / len(self._donations)


    @property
    def information(self):
        return (self._name, self.total_donations, self.num_donations, self.average_donations)

    def __str__(self):
        return "{}: {}".format(self._name, self._donations)


    def multiplier(self, factor):
        new_donations = list(map(lambda x: x*factor, self._donations))
        new_donor = Donor(self._name)
        new_donor.add_donations(new_donations)
        return new_donor


    def filter_multiplier(self, factor, min_donation=0, max_donation=-1):
        multiplier_donations = list(filter(lambda x: x > min_donation, self._donations))
        if max_donation != -1:
            multiplier_donations = list(filter(lambda x: x < max_donation, multiplier_donations))

        non_multiplier_donations = list(filter(lambda x: x not in multiplier_donations, self._donations))
        multiplier_donations = list(map(lambda x: x*factor, multiplier_donations))
        new_donations = multiplier_donations + non_multiplier_donations
        new_donor = Donor(self._name)
        new_donor.add_donations(new_donations)
        return new_donor

class DonorDB:

    def __init__(self):
        self._donors = {}


    def update_donor(self, donor):
        """
        update_donor update donor's donation, if a donor DNE, this method adds new one to the list
        """
        for donation in donor.donations:
            self._donors.setdefault(donor.name.lower(), Donor(donor.name)).add_donation(donation)


    def get_total_from_donor(self, donor_name):
        return self._donors[donor_name.lower()].total_donations


    def get_donor(self, donor_name):
        return self._donors[donor_name.lower()]


    def get_donor_information(self, donor_name):
        return self._donors[donor_name.lower()].information

    @property
    def list_donors(self):
        return [donor.name for _ , donor in self._donors.items()]

    @property
    def num_donors(self):
        return len(self._donors)


    def generate_sorted_report(self):
        return sorted([donor.information for _, donor in self._donors.items()], key=lambda item: item[1], reverse=True)

    @property
    def generate_printable_report(self):
        return ['{:20}{:>20}{:>12}{:>14}'.format(*donor_info) for donor_info in self.generate_sorted_report()]


    def __str__(self):
        return str(self._donors.keys())


    def __repr__(self):
        return str(self._donors)

    def donation_multiple(self, multiplier):
         new_donors = DonorDB()
         for _, donor in self._donors.items():
             new_donors.update_donor(donor.multiplier(multiplier))
         return new_donors

    def donation_filter_multiple(self, multiplier, min_donation=0, max_donation=-1):
        new_donors = DonorDB()
        for _, donor in self._donors.items():
            new_donors.update_donor(donor.filter_multiplier(multiplier, min_donation, max_donation))
        return new_donors

    def donor_projection(self, donor_nick, multiplier, min_donation=0, max_donation=-1):
        # ((self.get_donor(donor_nick)).filter_multiplier(multiplier, min_donation, max_donation)).total_donations
        current_donor = self.get_donor(donor_nick)
        new_donor = current_donor.filter_multiplier(multiplier, min_donation, max_donation)
        return new_donor.total_donations
