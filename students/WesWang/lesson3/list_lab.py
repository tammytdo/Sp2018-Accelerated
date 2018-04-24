#=========================================================================================
#Name: List Lab
#Author: Wesley Wang
#Date: 4/18/2018
#=========================================================================================

#Series 1
print("Series1:\n")
fruits = ["Apples", "Pears", "Oranges", "Peaches"]
print(fruits)
new_fruit = input("\nAdd Another Fruit of Your Choice:")
fruits.append(new_fruit.capitalize())
print(fruits)
pick = int(input("\nPlease Pick Your Favorite Fruit in the List(1-5):"))
print(fruits[pick-1])
print("\nAdded Papayas To the Beginning of the List with "+":")
fruits = ["Papayas"] + fruits
print(fruits)
print("\nAdded Watermelons To the Beginning of the List with Insert:")
fruits.insert(0, "Watermelons")
print(fruits)
print("\nDisplay All Fruits Starts with 'P':")
P_fruit = []
for item in fruits:
  if item not in P_fruit and item[0].lower() == "p":
    P_fruit.append(item)
print(P_fruit)

#Series2
print("\n\nSeries2:\n")
print(fruits)
print("\nLast Fruit Removed")
fruits.pop()
print(fruits)
while True:
  del_fruit = input("Pick a Fruit to Remove: ").capitalize()
  if del_fruit in fruits:
    fruits.remove(del_fruit)
    break
  else:
    print("Not in the List, Pick Another One!")
    continue
print(f"\n{del_fruit} Removed!")
print(fruits)

#Series3
print("\n\nSeries3:\n")
rmv_lst = []
for fruit in fruits:
  while True:
    choice = input(f"Do you like {fruit}? (yes/no)")
    if choice.lower() == "yes":
      print(f"{fruit} Kept!")
      break
    elif choice.lower() == "no":
      print(f"{fruit} Removed!")
      rmv_lst.append(fruit)
      break
    else:
      print("You can only pick yes or no!!")
      continue
for item in rmv_lst:
  fruits.remove(item)
print("\nRemaining Fruits:")
print(fruits)

#Series4
print("\n\nSeries4:\n")
print(fruits)
print("\nReverse Order:")
fruits = fruits[::-1]
print(fruits)
print("\nRemove Last Fruit:")
fruits.pop()
print(fruits)
