def test_circle_size():
    assert Circle(1) < Circle(2)

def test_circle_eq():
	assert Circle(2) == Circle(2)
	assert Circle(4) != Circle(2)