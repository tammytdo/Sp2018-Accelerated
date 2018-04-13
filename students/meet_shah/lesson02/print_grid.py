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
 

print_grid(3)
print_grid(4)
print_grid(5)
print_grid(6)
print_grid(15)

