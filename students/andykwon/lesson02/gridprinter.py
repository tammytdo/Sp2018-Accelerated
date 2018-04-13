def print_grid(num):
    for i in range(num):
        if i % 2 == 0:
            for j in range(num//2):
                print('+', end=' - ' * int(num/2))
                
            print('+')
        else:  
            for j in range(num//2):
                for k in range (num//2):
                    print('|', ' ', end=' ' * int(num-1))
                print('|')

        

print_grid(5)
