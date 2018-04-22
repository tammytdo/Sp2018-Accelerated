#=========================================================================================
#Name: String Formatting Lab
#Author: Wesley Wang
#Date: 4/18/2018
#=========================================================================================

#String Formatting Lab

tuple1 = ( 2, 123.4567, 10000, 12345.67)
tuple3 = (1,2,3,4,5,6)
tuple4 = ( 4, 30, 2017, 2, 27)
list5 = ['oranges', 1.3, 'lemons', 1.1]

def task1(tup):
  result = "file_{0}: {1:.2f}, {2:.2e}, {3:.2e}".format(*tup)
  return result

def task2(tup):
  result = "file_{0:003}: {1:.0f}, {2:.1e}, {3:.0f}".format(*tup)
  return result

def task3(tup):
  form_string = ", {:d}"*(len(tup)-1)
  result = f"The {len(tup)} numbers are {tup[0]}" + form_string.format(*tup[1:])
  return result

def task4(tup):
  result = "{3}, {4}, {2}, {0}, {1}".format(*tup)
  return result

def task5(lst):
  result = f"The weight of an {lst[0][:-1].upper()} is {lst[1]} and the weight of a {lst[2][:-1].upper()} is {lst[3]}"
  return result


print("Task 1: " + task1(tuple1))
print("Task 2: " + task2(tuple1))
print("Task 3: " + task3(tuple3))
print("Task 4: " + task4(tuple4))
print("Task 5: " + task5(list5))