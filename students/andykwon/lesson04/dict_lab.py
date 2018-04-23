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

# Dictionaries 2

for key in lst:
    i = 0
    for letter in (lst[key]):
        if letter.upper() == "T":
            i += 1
    lst[key] = i

print(lst)

# Sets 1
s2 = set([0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
s3 = set([0, 3, 6, 9, 12, 15, 18])
s4 = set([0, 4, 8, 12, 16, 20])

print(s2)
print(s3)
print(s4)

# Subsets?
print(set(s2) < set(s3))
print(set(s4) < set(s2))
# OR
print(s2.issubset(s4))
print(s4.issubset(s2))

# Sets 2

s = set(['P', 'y', 't', 'h', 'o', 'n', 'i'])
fs = frozenset(('m', 'a', 'r', 'a', 't', 'h', 'o', 'n'))

print(s.union(fs))
print(s.intersection(fs))
