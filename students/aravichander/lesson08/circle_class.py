from math import pi 
circlelist = []

#Creating class to represent circle object 
class Circle:
	def __init__(self,radius):
		if radius == 0:
			raise ValueError
		elif radius < 0:
			raise ValueError
		else:
			self.radius = radius
			#print("Circle with radius {0:.6f}".format(radius))
	
	def __str__(self):
		return "Circle with radius {0:.6f}".format(self.radius)

	def __repr__(self):
		return "Circle({})".format(self.radius)
	
	@property
	def diameter(self):
		return self.radius*2

	@diameter.setter
	def diameter(self,diameter):
		self.radius = (diameter)/2

	@property
	def area(self):
		return pi*(self.radius**2)
		#print("Area of circle is {0:.2f}".format(area))

	#not fully understanding this but hoping I did this correctly!
	@classmethod
	def circle_from_diameter(cls, diameter):
		radius = diameter/2
		return cls.Circle(radius)

	def addcircle(self):
		
	
	#being able to add 2 new circles together
	def __add__(self,newcircle):
		if isinstance(newcircle,Circle):
			return Circle(self.radius + newcircle.radius)
		else:
			return Circle(self.radius + newcircle)

	def __mul__(self,factorint):
		return Circle(self.radius*factorint)

	def __eq__(self,other):
		return self.radius == other.radius

	def __lt__(self,other):
		return self.radius < other.radius

	def __gt__(self,other):
		return self.radius > other.radius




c =Circle(3)
# print(c)
# print(repr(c))
c2 = Circle(4)
# print(repr(c+c2))
# print(c*2)

print(c == c2)
print(c < c2)
print(c > c2)
print(c == Circle(5))



#user queries class to output attributes of circle 

