#print grid with single variable

# declaring grid variables

plus = '+'

minus = ' - '

line = '|'

space = '   '

#Building function to build a single variable print function 

def print_grid(n):
    count = n
    centerrow = ((n)//2)+1
    center = ((n)//2)-1
    row = (plus + (minus*center) + plus + (minus*center) +plus)
    column = (line + (space * center) + line + (space * center) +line)
    
    while count >= 1:
        if count ==1:
            print(row)
        elif count == n:
            print(row)
        elif count == centerrow:
            print(row)
        else:
            print(column)
        count = count - 1
        
    

#run function print_grid

print_grid(15)
    

#Building function to build a multiple variable print function





