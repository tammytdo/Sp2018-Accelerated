def grid(x):
    y = int(x/2)
    point = '+'
    s1 = ' -'*y+' '
    s2 = '  '*y+' '
    line = point
    line2 = '|'
    for i in range(2):
        line += s1+point
        line2 += s2+'|'

    print (line)
    def graph(y):
        for i in range(y):
            print (line2)
        print(line)
    for i in range(2):
        graph(y)
