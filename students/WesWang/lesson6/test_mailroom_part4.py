import mailroom_part4 as mail
import pytest

def test_thank_letter():
    letter = mail.thank_letter("Donor X", 500)
    assert "$500.00" in letter


def test_report():
    report = mail.build_report()
    assert "Donor A" and "140,000" in report

