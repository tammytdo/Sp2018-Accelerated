#print grid with single variable

# declaring grid variables

plus = '+'

endplus = '+'

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

#print_grid(15)
    

#Building function to build a multiple variable print function

mrow = (plus + (minus*3))
midrow = (plus + (minus*3))
newrow = mrow+midrow+plus
mcolumn = (line + (space *3))
midcolumn = (line + space *3)
newcolumn = mcolumn + midcolumn + line
mrows = newrow
mcolumns = newcolumn 

#print(mrows)
#print(mcolumns)
#print(mcolumns)
#print(mcolumns)
#print(mrows)

def print_grid2(n,m):
    unitcount = (m * n)+(n+1)
    gridcount = n
    mrow = (plus + (minus*m))
    midrow = (plus + (minus*m))
    newrow = mrow+endplus
    endrow = endplus
    mcolumn = (line + (space *m))
    midcolumn = (line + space *m)
    newcolumn = mcolumn + midcolumn + line
    
    while unitcount >= 1:
        if unitcount ==1:
            print(newrow + ((newrow[1:])*(n-1)))
        elif unitcount == m:
            print(newrow + ((newrow[1:])*(n-1)))
        elif unitcount % m == 0:
            print(newrow + ((newrow[1:])*(n-1)))
        else:
            print(newcolumn)
        unitcount = unitcount - 1
        
    

#run function print_grid

print_grid2(3,4)
    

#Building function to build a multiple variable print function



