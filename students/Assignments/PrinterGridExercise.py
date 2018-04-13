#print grid with single variable

plus = '+'

minus = '-'

line = '|'

space = ' '

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


def print_grid(n):
    yolo = ((n-1)//2)
    row = (plus+minus*yolo+plus+minus*yolo+plus)
    column = (line+space*yolo+line+space*yolo+line)
    
    while n > 0:
        if n ==1 or n == yolo or n ==15:
            print(row)
        n = n - 1
    print ('done') 


print_grid(3)
    



