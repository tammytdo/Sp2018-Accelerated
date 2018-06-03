
	#Series 1


Fruit = ["Apples","Pears", "Oranges", "Peaches"]
print(Fruit)
response = input("Think of another fruit!\n")
Fruit.append(response)
print(Fruit)
response2 = int(input("Give me a number\n"))
print(response2)
print(Fruit[response2-1])
response3 = input("Give me one more fruit\n")
Fruit2 = response3.split()
AllFruits = Fruit2 + Fruit
print(AllFruits)
response4 = input("Last fruit I swear\n")
AllFruits.insert(0,response4)
print(AllFruits)
listlen = len(AllFruits)
print("Length of list is",listlen,"items long")

# for x in range(0,listlen):
# 	if AllFruits[x][0] == "P":
# 		print(AllFruits[x])


#Series 2
# print(AllFruits)
# del AllFruits[listlen-1]
# print(AllFruits)
# Fruitdelete = input("Which fruit do you want to remove?\n")
# DelPosition = AllFruits.index(Fruitdelete)
# del AllFruits[DelPosition]
# print(AllFruits)

#Series3

AllFruits2 = AllFruits
for i in range(0,listlen):
	response4 = input("Do you like" + AllFruits[i] + "?")
	if response4 == "No":
		#AllFruits2.remove(AllFruits[i])
		print(AllFruits2)
	if response4 == "Yes":
		print(AllFruits2)

print(AllFruits2)

# #Series 4
# Reversefruit = []
# for fruit in AllFruits:
# 	Reversefruit.append(fruit[::-1])

# print(Reversefruit)
# del(AllFruits[listlen-1])
# print(AllFruits)


