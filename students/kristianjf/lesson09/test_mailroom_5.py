#!/usr/bin/env python3

import mailroom_5 as m5

def test_donor():
    kf = m5.Donor('Kristian Francisco', [1000, 100])
    kf.metrics()
    assert kf.name == 'Kristian Francisco'
    assert kf.num_d == 2
    assert kf.total_d == 1100
    assert kf.avg_d == 550.0

def test_donor_handle():
    kf = m5.Donor('Kristian Francisco', [1000, 100])
    dh = m5.DonorsHandle()
    dh.add_donor(kf)
    assert dh.DATA_STRUCTURE[0][0] == 'Kristian Francisco'
    assert dh.DATA_STRUCTURE[0][1] == [1000, 100]
    assert dh.DATA_STRUCTURE_DICTS[0] == {'name': 'Kristian Francisco', 'donation': [1000, 100]}
