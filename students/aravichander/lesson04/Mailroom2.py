#Mailroom #2

import sys
import json


#Modified into a dictionary

Donors = {"Bill Gates":[10000,12000],
		  "Jeff Bezos":[50],
		  "Mark Zuckerberg": [500,600,700],
		  "Paul Allen": [250,350,450],
		  "King of Siam": [200,250]
		  }

# Donors = {"Bill Gates":("Bill Gates",[10000,12000]),
# 		  "Jeff Bezos":("Jeff Bezos",[50]),
# 		  "Mark Zuckerberg": ("Mark Zuckerberg",[500,600,700]),
# 		  "Paul Allen": ("Paul Allen",[250,350,450]),
# 		  "King of Siam": ("King of Siam",[200,250])
# 		  }

def printdonors():
	for x,v in Donors.items():
		print(x,"donated",v)
		#print(Donors[x])
#for x in Donors:
#     print (x)
#     for y in Donors[x]:
#         print (y,':',Donors[x][y])

def thankall():
	for x in Donors:
		#print(x)
		#print(Donors[x])
		totaldonated = sum(Donors[x])
		#print(totaldonated)
		letterofthanks(x,totaldonated)
	
	# for donor in Donors:
	# 	print("Thankall function called - The donor is",donor,"and the amount donated is")
	# 	totaldonated = sum(Donors[donor])
	# 	letterofthanks(donor,totaldonated)


def letterofthanks(donorname,totaldonated):
	#To add sum of donations
	#print("This is running dear god please work")
	filename = donorname+".txt"
	f = open(filename,"w+")
	statementtowrite = "Thank you "+donorname+" for your donation of $"+str(totaldonated)+". We greatly appreciate your help."
	f.write(statementtowrite)
	f.close()
	print("\nLetter of thanks has been saved to hard disk as text file under "+str(filename))

def searchdonors(thankdonor):
	#print("Searching for donor")
	for x in Donors:
		#print(x)
		if thankdonor == x:
			#print("Found donor")
			totaldonated = sum(Donors[x])
			#print(totaldonated)
			letterofthanks(thankdonor,totaldonated)


def newdonation():
	newdonor = input("Input name of new donor")
	#modify to be able to take multiple donations
	newdonations = input("Input donations, multiple if necessary")

def thanks():
	thankdonor = input("\nPlease enter full name of donor you'd like to thank or list to view donors\n")
	if thankdonor == "list":
		printdonors()
		thanks()
	else:
		searchdonors(thankdonor)

def report():
	sorteddonors = sorted(Donors)
	print(sorteddonors)
	#Initial attempt at sorting dictionary - didn't realize it was this simple and this could have gone into my first mailroom!
	# sorteddonors = Donors.sort(key= lambda x:x[1])
	# print(sorteddonors)
	# print("\nHere's the report")

def mainloop():
	print("Introducing Mailroom!")
	response = "0"
	while response < "4":
		print("\nWhat do you want to do?")
		print("\n(1) Send a thank you\n", "(2) Create a Report,\n", "(3) Send letters to everyone,\n","(4) Quit")
		response = input(">> ")
		print("response was,",response)
		if response =="1":
			print("\nYou have chosen the 'Thank' option")
			thanks()
		elif response == "2":
			report()
		elif response == "3":
			thankall()
		else:
			print("\nSee you later!")
			sys.exit

mainloop()
# if __name__ == "__main__,":
# 	mainloop()