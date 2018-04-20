#This definitely did not work the way I wanted it to and I ran out of time before I could fix it!

plus = "+"
minus = "-"
vertical = "|"
n = int(input("Enter an odd number"))
defaultn = int((n-1)/2)
spacen = (n-1)/2
defaultline = plus + minus*(defaultn) + plus + minus*(defaultn) + plus

print(defaultline)
for x in range(0,defaultn):
	print(vertical,""*n,end="")
	print(vertical,""*n,end="")
	print(vertical,end="\n",)

print(defaultline)
# for x in range(0,defaultn):
# 	print(verticaldash," "*defaultn,verticaldash," "*defaultn,verticaldash)

print(defaultline)
print(ord(plus))
print(ord(minus))
print(ord(verticaldash))


