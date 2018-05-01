
import mailroom

'''
TEST_DATA = test_data()
def test_1():
    result = create_donors_report(TEST_DATA)
    
    print(result)
    
    assert len(result) == len(TEST_DATA)
    donor = result[1]
    assert donor[-1] == donor[1] / donor[2]
    
    assert result[0][2] > result[-1][1]
'''    
#def retrieve_donations(fullname):
#    """ if donors exists, return donations, otherwise return None"""
#    if fullname in DONORS:
#        return DONORS[fullname]

def test_retreive_donations():
    result = mailroom.retrieve_donations('John Smith')
    print(result)
    assert result == [25,25]
#    assert False
    
def test_notget_donations():
    result = mailroom.retrieve_donations('Mathew Martin')
    assert result is None

# def add_donation(fullname, amount):
#    DONORS.setdefault(fullname, []).append(amount)


def test_add_donation():
    result = mailroom.add_donation('Ed Shingles', amount=25)
    assert result is None

"""
This Mailroom includes some exception testing already for the selection main loop 
functionality.

def select_action(arg_dict, ans):
    try:
        return arg_dict[ans]()
    except (KeyError):
        return False
"""

