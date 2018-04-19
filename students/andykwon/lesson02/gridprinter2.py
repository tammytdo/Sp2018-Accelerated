def print_grid2(num1, num2):

    for i in range(num1):
        
        for j in range (num1):
            print(end='+' + ' - ' * num2)
        
        print('+')
        
        for k in range(num2):

            for j in range (num1):
                print(end='|' + ' ' * int(num2 * 3))

            print('|')

    for j in range (num1):
        print(end='+' + ' - ' * num2)
        
    print('+')

print_grid2(5,3)