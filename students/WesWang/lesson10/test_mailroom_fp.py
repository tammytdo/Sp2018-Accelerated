import mailroom_fp as mr
from mailroom_fp import Donor
import pytest

test = []
test1 = Donor("Test1", [100,200])
test2 = Donor("Test2", [500,1200])
test.extend([test1, test2])

def test_class():
    donor = Donor("Class", [100, 200, 300])
    print(donor)

def test_add_donor():
    mr.add_donor("Fake Donor", 1000)
    assert mr.donors[-1].total == 1000

def test_thank_letter():
    letter = mr.thank_letter(test1.name, test1.donations[0])
    assert "Test1" in letter