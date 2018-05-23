#Mailroom #2

import sys
import json
import unittest 

Donors = {"Bill Gates":[10000,12000],
		  "Jeff Bezos":[50],`
		  "Mark Zuckerberg": [500,600,700],
		  "Paul Allen": [250,350,450],
		  "King of Siam": [200,250]
		  }

def printdonors():
	for x,v in Donors.items():
		print(x,"donated $",v)

def thankall():
	for x in Donors:
		totaldonated = sum(Donors[x])
		letterofthanks(x,totaldonated)

def letterofthanks(donorname,totaldonated):
	#To add sum of donations
	filename = donorname+".txt"
	f = open(filename,"w+")
	statementtowrite = "Thank you "+donorname+" for your donation of $"+str(totaldonated)+". We greatly appreciate your help."
	f.write(statementtowrite)
	f.close()
	print("\nLetter of thanks has been saved to hard disk as text file under "+str(filename))

def searchdonors(thankdonor):
	#Not sure if these exceptions here are needed to be honest#
	for x in Donors:
		try:
			if thankdonor == x:
				totaldonated = sum(Donors[x])
				letterofthanks(thankdonor,totaldonated)
		except KeyError:
			print("That donor doesn't exist")

#Needs to be modified to actually add something to original list
def newdonation():
	newdonor = input("Input name of new donor")
	#modify to be able to take multiple donations
	newdonations = input("Input donations, multiple if necessary")

def thanks():
	thankdonor = input("\nPlease enter full name of donor you'd like to thank or list to view donors\n")
	#Added to catch name errors #
	try:
		if thankdonor == "list":
			printdonors()
			thanks()
		else:
			searchdonors(thankdonor)
	except NameError:
		print("That donor doesn't exist, try again")

def report():
	sorteddonors = sorted(Donors)
	print(sorteddonors)


def mainloop():
	print("Introducing Mailroom!")
	response = "0"
	try:
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
	except ValueError:
		print("Not an option, try again!")



mainloop()
