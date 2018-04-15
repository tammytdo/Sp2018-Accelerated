#Upload to GIT Test


#step 1

#Test figures 
# F00 = 0,  F01 = 1,  F02 = 1,  F03 = 2,  F04 = 3,   F05 = 5,  F06 = 8,  F07 = 13
# F08 = 21, F09 = 34, F10 = 55, F11 = 89, F12 = 144, F13 = 233 F14 = 377 F15 = 610


def fibinacci_series (n):
    if n == 1 or n == 2:
        return (1)
    return fibinacci_series (n-1) + fibinacci_series (n-2)



print(fibinacci_series(5))

#step 2 

#Test figures 
# F00 = 0,  F01 = 1,  F02 = 1,  F03 = 2,  F04 = 3,   F05 = 5,  F06 = 8,  F07 = 13
# F08 = 21, F09 = 34, F10 = 55, F11 = 89, F12 = 144, F13 = 233 F14 = 377 F15 = 610

def lucas_series (n):
    if n == 0: 
        return (2)
    elif n == 1:
        return(1)
    return lucas_series (n-1) + lucas_series (n-2)

print(lucas_series(5))