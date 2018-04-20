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
 
def help_print_line(startpattern, endpattern, repeat):
    for i in range(0,repeat):
        print(startpattern, end='')
    print(endpattern)

def print_grid2(box_repeat,grid_repeat):

    topstart = "+ "
    topmid   = "- "
    topend   = "+"

    midstart = "| "
    midmid   = "  "
    midend   = "|"

    pattern1 = topstart + topmid*grid_repeat
    pattern1end = topend
    
    pattern2 = midstart + midmid*grid_repeat
    pattern2end = midend

    for i in range(0,box_repeat):
        help_print_line(pattern1, pattern1end, box_repeat)
        for i in range(0,grid_repeat):
            help_print_line(pattern2, pattern2end, box_repeat)

    help_print_line(pattern1, pattern1end, box_repeat)


print_grid2(0,0)
print_grid2(3,4)
print()
print_grid2(5,10)
print()

