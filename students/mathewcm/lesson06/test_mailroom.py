
import mailroom


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

 

    