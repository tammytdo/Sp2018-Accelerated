#print grid with single variable

plus = '+'

minus = '-'

line = '|'

space = ' '

#Building function to build a single variable print function 

def print_grid(n):
    count = n
    yolo = ((n-1)//2)
    center = ((n-1)//2)-1
    row = (plus + (minus*center) + plus + (minus*center) +plus)
    column = (line + (space * center) + line + (space * center) +line)
    
    while count >= 1:
        if count ==1:
            print(row)
        elif count == n:
            print(row)
        elif count == yolo:
            print(row)
        else:
            print(column)
        count = count - 1
        
    

#run function print_grid

print_grid(11)
    



    

#rows occur for 1, (n-1)/2, or when n = n (i.e. the last row)

#    for (n == 1 or n == yolo or n = n)
#        print(row)
#    elif
#        print(column)
    #for n in range (1,n):
        #if n ==[1,yolo,n]:  
            #print(row)
    #else: 
        #print(column)



