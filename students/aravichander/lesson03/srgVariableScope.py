val="A" #this is global variable

def myFx():
	val="B" #this is local variable
	print("[myFx] value is: "+val)

def myFx2():
	print("[myFx2] value is: "+val)

def myFx3():
	global val
	val ="thisWasChangedInsideAFx"
	print("[myFx3] value is: "+val)

print("[main] value is: "+val)
myFx()
myFx2()

val="thisIsNew!"
print("[main] value is: "+val)
myFx()
myFx2()

myFx3()
print("[main] value is: "+val)
myFx()
myFx2()


