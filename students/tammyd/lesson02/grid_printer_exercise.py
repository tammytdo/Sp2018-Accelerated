''' Grid Printer Exercise '''

plus = "+"
minus = "-"
pipe = "|"

"""
#Part 1: Write a function that draws a grid
print("+ - - - - + - - - - +")
print("|         |         |")
print("|         |         |")
print("|         |         |")
print("|         |         |")
print("+ - - - - + - - - - +")
print("|         |         |")
print("|         |         |")
print("|         |         |")
print("+ - - - - + - - - - +")


print("\n")




#Part 2: def function to print a grid
def print_grid_horizontal(n):
    print((plus + " -"* (n// 2) + " " + plus + " ")+("- "* (n//2) + plus))

def print_grid_vertical(n):
    for i in range (n//2):
        print(pipe + " "*n + pipe + " "*n + pipe)

n = 15
print_grid_horizontal(n)
print_grid_vertical(n) 
print_grid_horizontal(n)
print_grid_vertical(n)
print_grid_horizontal(n)

print("\n")

"""

#Part 3: A function with two parameters
def print_grid2(x,y):
    string1 = ("+ " + "- " * y) * x + "+"
    string2 = ("| " + "  " * y) * x + "| \n"
    for i in range(x):
        print(string1)
        print(string2 * y,end="")
    print(string1)


print_grid2(3,4)
