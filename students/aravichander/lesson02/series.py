def fibonacci(position):
	if position == 1:
		return 0
	elif position == 2:
		return 1
	else:
		return (fibonacci(position -1)+fibonacci(position-2))


def lucas(position):
	if position == 1:
		return 2
	elif position == 2:
		return 1
	else:
		return (lucas(position -1)+lucas(position-2))


def sum_series(position, value1=0, value2=1):
	if position == 1:
		return value1
	elif position == 2:
		return value2
	else:
		return (sum_series(position - 1,value1,value2)+sum_series(position-2,value1,value2))

#Testing for fibonacci errors, ensuring starting numbers have no issues!
assert fibonacci(1) == 0
assert fibonacci(2) == 1
assert fibonacci(4) == 2

#Similar testing for lucas series 
assert lucas(1) == 2
assert lucas(2) == 1
assert lucas(3) == 3
assert lucas(4) == 4
assert lucas(5) == 7

#Testing to see if default conditions for sum_series work
assert sum_series(4) == 2
#The following test was to see if non-default values work
assert sum_series(4,0,1) == 2
#Testing to see if non-default, non-fibonacci (lucas) values work
assert sum_series(3,2,1) == 3
#Testing non-lucas, non-fibonacci values
assert sum_series(3,10,20) == 30





		
	
	

		
		
		