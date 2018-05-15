"""create a circle using python"""

import math

#step 1: create a class
class Circle():
    #the radius is a required parameter 
    def __init__(self, radius):
        self.radius = radius
    def radius(self):
        radius = self.radius
        return radius


#attribute for the radius
#c1.radius
#c2.radius

#c1 = Circle(the_radius)



#Step 2: add a “diameter” property, so the user can get the diameter
    @property
    def diameter(self):
        return self._radius * 2

#Step 3: Set up the diameter property so that the user can set the diameter of the circle:
    @diameter.setter
    #program requires a "def diameter" twice, correct?
    def diameter(self, value):
        self._radius = value

#Step 4: Add an area property so the user can get the area of the circle
    @property
    def area(self):
        #A = pi*r^2
        return math.pi * (self._radius ** 2)

#Step 5: Add an “alternate constructor” that lets the user create a Circle directly with the diameter
    def from_diameter(diameter):
        radius = diameter / 2
        return (radius**2) * math.pi

#Step 6: Add __str__ and __repr__ methods to your Circle class.
    def __str__(self):
        return "Circle with radius: ", str(self._radius)



#instances of radius
c1 = Circle(4)
c2 = Circle(5) 



#c = Circle()
#Step 3: user can set the diameter of the circle:
c1.diameter = 10
print("radius:", c1.radius)
print("user defined diameter:",c1.diameter)
print("user defined radius:",c1._radius)
print("user defined area:", c1.area)
#this diameter assignment seems incorrect to me. need help resolving
diameter = Circle.from_diameter(10)
print("area from diameter:", c1.diameter)

print("Step 6:", str(c1.radius))


#in progress. moving on to additional assignments