def print_grid(x):
    topstart = "+ "
    topmid   = "- "
    topend   = "+"

    midstart = "| "
    midmid   = "  "
    midend   = "|"

    repeat = int(x/2)
    topline = topstart + topmid*repeat + topstart + topmid*repeat + topend
    midline = midstart + midmid*repeat + midstart + midmid*repeat + midend
    
    print(topline)
    for i in range(0,2):
        for i in range(0,repeat):
            print(midline)
        print(topline)
 

def print_grid2(x,y):

    box_repeat = x
    grid_repeat = y 
    topstart = "+ "
    topmid   = "- "
    topend   = "+"

    midstart = "| "
    midmid   = "  "
    midend   = "|"

    pattern1 = topstart + topmid*y
    pattern1end = topend
    
    pattern2 = midstart + midmid*y
    pattern2end = midend

    for i in range(0,grid_repeat):
        print(pattern1, end='')

print_grid2(3,4)
print()
print_grid2(10,10)
print()

