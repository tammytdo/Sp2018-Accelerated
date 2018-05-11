#!/usr/bin/env python

#Unit testing

import os
import mailroom_pt4 as mailroom

mailroom.donor_db = mailroom.donor_db

#Lots of failures but I did my best to show my work.
#Is it necessary to test every single function?



menu_dict = mailroom.main_menu()
menu_selection = menu_dict("T")


def test_donor_database():
    assert return donor_database == donor_db
    

#what is causing this error?: 
#"NameError: name 'menu_dict' is not defined"
def test_main_menu():
    menu_selection = mailroom.main_menu("T")
    assert menu_dict[0] == "T"
    assert letters_to_everyone in menu_dict


#what is causing this failure?: 
#"TypeError: 'NoneType' object is not subscriptable"
def test_find_donor():
   donor = mailroom.find_donor("queeN bey")
   assert donor[0] == "Queen Bey" 
#   donor = mailroom.find_donor("mandy MOOre")
#   assert donor[0] == "Mandy Moore"

#Why does this pass even when I test "qenn bey" instead of "Queen Bey"?
def test_find_donor_not():
    "test one that's not there"
    donor = mailroom.find_donor("qenn bey")
    assert donor is None

donor_name = "Jessica Simpson"
def test_ty_letter(donor_name):
#     # donor_name = mailroom.thank_you()
#     # donor_name = "Jessica Simpson"
    donor = ("Jessica Simpson", [50.99, 100.99, 4000.99])
    ty_letter = mailroom.ty_letter(donor)
    assert ty_letter.startswith("Dear Jessica Simpson")
    assert ty_letter.endswith("An Academy Student\n")
    assert mailroom.find_donor(donor) == donor

def test_create_report():
    report = mailroom.create_report()
    assert report.startswith("Menu: Create a Report\n")


if __name__ == "__main__":
    test_find_donor()
    test_find_donor_not()
    test_ty_letter()
    test_create_report()