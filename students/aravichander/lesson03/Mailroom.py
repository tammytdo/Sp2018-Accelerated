#simple mailroom program 

Donors = [("Bill Gates",[10000,12000]),
		  ("Jeff Bezos",[50]),
		  ("Mark Zuckerberg",[500,600,700]),
		  ("Paul Allen",[250,350,450]),
		  ("King of Siam",[200,250])
		  ]

def printdonors():
	for x in Donors:
		print(x[0])


def letterofthanks(donorname,totaldonated):
	#To add sum of donations
	print("\nThank you",donorname,"for your donation of $",totaldonated)

def searchdonors(thankdonor):
	#print("Searching for donor")
	for x in Donors:
		if thankdonor == x[0]:
			totaldonated = sum(x[1])
			letterofthanks(thankdonor,totaldonated)

#def adddonor():

def thanks():
	thankdonor = input("\nPlease enter full name of donor you'd like to thank or list to view donors\n")
	if thankdonor == "list":
		printdonors()
		thanks()
	else:
		searchdonors(thankdonor)

def report():
	#not sure why this isn't working as well as I'd like it to 
	sorteddonors = Donors.sort(key= lambda x:x[1])
	print(sorteddonors)
	print("\nHere's the report")

def mainloop():
	print("Introducing Mailroom!")
	response = "0"
	while response < "3":
		print("\nWhat do you want to do?")
		print("\n(1) Send a thank you\n", "(2) Create a Report,\n", "(3) quit")
		response = input(">> ")
		print("response was,",response)
		if response =="1":
			print("\nYou have chosen the 'Thank' option")
			thanks()
		elif response == "2":
			report()
		else:
			print("\nSee you later!")
			quit 

mainloop()
# if __name__ == "__main__,":
# 	mainloop()