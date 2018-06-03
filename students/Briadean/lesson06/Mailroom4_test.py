#!/usr#!/usr/bin/env python3

import os
from contextlib import redirect_stdout
import Mailroom4 as Mailroom
import io


def test_accept_donation():
    Mailroom.accept_donation(name="Bri")
    assert "Bri" in Mailroom.donors_dict.keys()


def test_list_donors():
    file = io.StringIO()
    with redirect_stdout(file):
        print(Mailroom.list_donors())
    contents = file.getvalue()
    try:
        assert ("Retsuko Rarecho" and
                "Fenneko Inoue" and
                "Haida Kato" and
                "Gori Tsuruta" and
                "Washimi Koiwasaki") in contents
    finally:
        file.close()


def test_generate_report():
    file = io.StringIO()
    with redirect_stdout(file):
        print(Mailroom.generate_report())
    contents = file.getvalue()
    try:
        for name, donation in Mailroom.donors_dict.items():
            assert name in contents
            assert str(sum(donation)) in contents
            assert str(len(donation)) in contents
    finally:
        file.close()


def test_write_letters_disk():
    files = Mailroom.write_letters_disk()
    disk_files = os.listdir()
    # Complaining path not specified, throwing TypeError 'NoneType' not iterable for line 47.I thought this defaults CWD
    assert [file in disk_files for file in files]


test_accept_donation()
test_list_donors()
test_generate_report()
test_write_letters_disk()
