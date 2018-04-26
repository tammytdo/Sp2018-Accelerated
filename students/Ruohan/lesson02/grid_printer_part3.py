def grid2(x,y):
    point = '+'
    s1 = ' -'*y+' '
    s2 = ' '*(y*2)+' '
    line = point
    line2 = '|'
    for i in range(x):
        line += s1+point
        line2 += s2+'|'
    print (line)

    def graph(x):
        x = y
        for i in range(x):
            print (line2)
        print(line)
    for i in range(x):
        graph(x)
