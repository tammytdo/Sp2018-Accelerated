def print_grid(x):
    n = x // 2
    m = n // 2
    a = '+ '
    b = '- ' * n
    c = '| '
    d = '  ' * n
    x = str('{}{}{}{}{}\n').format(a, b, a, b, a)
    y = str('{}{}{}{}{}\n').format(c, d, c, d, c)
    print(x+y*n+x+y*n+x)

print_grid(15)

def print_grid(length=1,width=1):
    a = '+ '
    b = '- ' * 4
    c = '| '
    d = '  ' * 4
    x = str('{}{}\n').format(a, b)
    y = str('{}{}\n').format(c, d)
    cap_x = str('{}\n').format(a)
    print(length*x+x+width*y)
print

#Note = Exercise is to print length * width based on first input and number of lines within each square by second input
