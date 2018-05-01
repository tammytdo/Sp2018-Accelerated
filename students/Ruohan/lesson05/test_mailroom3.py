"""
test code for mailroom3
"""

import mailroom3 as mr

def test_donors_name_list():
    donors = mr.donors_name_list()
    print(donors)
    assert 'William Gates III' in donors
    assert 'Jeff Bezos' in donors
    assert len(donors) == len(mr.old_datas)

