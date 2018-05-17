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
			print("Circle with radius {0:.6f}".format(radius))
	
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
	
	#being able to add 2 new circles together
	def __add__(self,newcircle):
		if isinstance(newcircle,Circle):
			return self.radius + newcircle.radius
		else:
			return self.radius + newcircle

	

	# def repr():
	


c =Circle(3)





#user queries class to output attributes of circle 

