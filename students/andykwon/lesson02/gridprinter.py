def print_grid(num):
    print('+' + ' - ' * int(num / 2) + ' + ' + ' - ' * int(num / 2) + '+')

    for i in range(int(num / 2)):
        print('| ' + ' ' * int(num / 2) * 3 +
              '|' + ' ' * int(num / 2) * 3 + ' |')

    print('+' + ' - ' * int(num / 2) + ' + ' + ' - ' * int(num / 2) + '+')

    for i in range(int(num / 2)):
        print('| ' + ' ' * int(num / 2) * 3 +
              '|' + ' ' * int(num / 2) * 3 + ' |')

    print('+' + ' - ' * int(num / 2) + ' + ' + ' - ' * int(num / 2) + '+')


print_grid(15)
