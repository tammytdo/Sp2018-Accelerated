def grid(x):
    y = int(x/2)
    point = '+'
    s1 = ' -'*y+' '
    s2 = '  '*y+' '
    line = point
    line1 = ' '
    line2 = '|'
    for i in range(2):
        line = line+s1+point
        line1 = line1+s2+' '
        line2 = line2+s2+'|'

    print (line)
    def graph(y):
        for i in range(y):
            print (line1)
            print (line2)
        print(line1)
        print(line)
    for i in range(2):
        graph(y)
