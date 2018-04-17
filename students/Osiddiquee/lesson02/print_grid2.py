def print_grid2(x,y):
    border = '+'
    interior = '|'
    for n in range (0,x):
        for n in range (0,y):
            border += ' -'
        border += ' +'
    for n in range (0,x):
        for n in range (0,y*2):
            interior += ' '
        interior += ' |'
    print(border)
    for n in range (0,x):
        for n in range (0,y):
            print(interior)
        print(border)
