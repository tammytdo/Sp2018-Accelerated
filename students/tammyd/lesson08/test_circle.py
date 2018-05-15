from circle import Circle

#instances
c1 = Circle(4)
c2 = Circle(5)

#why does this return None?
def test_radius_att():
    assert c1.radius == 4
    assert c2.radius == 5

print(test_radius_att())


#moving on to additional assignments