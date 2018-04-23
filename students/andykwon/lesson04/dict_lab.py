#$ ./dict_lab.py

# Dictionaries 1

lst = {"name": "Chris",
       "city": "Seattle",
       "cake": "Chocolate"
      }

print(lst)

lst.pop("cake")

print(lst)

lst["fruit"] = "Mango"

print(lst.keys())

print(lst.values())

print(("cake" in lst))

print(("Mango" in lst.values()))