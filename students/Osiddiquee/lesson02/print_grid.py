def print_grid(n):
    border = '+' + n//2*' -' + ' +' + n//2* ' -' + ' +'
    if n % 2 == 0:
        interior = '|' + (n+1)*' ' + '|' +  (n+1)*' ' + '|'
    else:
        interior = '|' + n*' ' + '|' +  n*' ' + '|'
    print(border)
    for x in range(0,n//2):
        print(interior)
    print(border)
    for x in range(0,n//2):
        print(interior)
    print(border)
