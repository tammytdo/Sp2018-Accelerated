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
    for i in range(0,repeat):
        print(midline)
    print(topline)
 

print_grid(3)
print_grid(4)
