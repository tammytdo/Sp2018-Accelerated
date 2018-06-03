#Upload to GIT Test


#step 1 - Runs the Fibonacci series assuming that F0 = 0, F1 = 1, and F2 = 2. Printing
#the following function (fibinacci_series(15)) will provide the corresponding fibinacci
#number. 

#Test figures 
# F00 = 0,  F01 = 1,  F02 = 1,  F03 = 2,  F04 = 3,   F05 = 5,  F06 = 8,  F07 = 13
# F08 = 21, F09 = 34, F10 = 55, F11 = 89, F12 = 144, F13 = 233 F14 = 377 F15 = 610


def fibinacci_series (n):
    if n == 0:
        return (0)
    elif n == 1 or n == 2:
        return (1)
    return fibinacci_series (n-1) + fibinacci_series (n-2)



print(fibinacci_series(15))

#step 2 

#Test figures 
# L00 = 2,  L01 = 1,  L02 = 3,  L03 = 4,  L04 = 7,   L05 =11,  L06 = 18, L07 = 29
# L08 = 47, L09 = 76, L10 = 123,L11 = 199,L12 = 322, L13 = 521 L14 = 843 L15 = 1364

def lucas_series (n):
    if n == 0: 
        return (2)
    elif n == 1:
        return(1)
    return lucas_series (n-1) + lucas_series (n-2)

print(lucas_series(15))

#step 3 

#Calls the defined functions above

def sum_series1 (n,lucas0=None,lucas1=None):
    if lucas0 ==2 and lucas1 == 1:
        return lucas_series(n)
    else:
        return fibinacci_series(n)

print(sum_series1(15,2,1))

# Build sum_series without lucas and fibonacci functions 

def sum_series (n,lucas0=None,lucas1=None):
    m = n 
    if lucas0 == 2 and lucas1 ==1 and m == 0:
            return (2)
    elif m == 1 :
        return (1)
    elif m == 0:
        return(0) 
    else:   
        return sum_series (m -1) + sum_series (m -2) 


print(sum_series(15,2,1))

