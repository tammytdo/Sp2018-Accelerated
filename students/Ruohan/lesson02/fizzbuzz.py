for i in range(1, 101):
    if i % 3==0 and i % 5==0:
        print('FizzBuzz')
    elif i % 3==0:
        print('Fizz')
    elif i % 5==0:
        print('Buzz')
    else:
        print (i)


for i in range(1, 101):
    s = ''
    if i % 3==0:
        s = 'Fizz'
    if i % 5==0:
        s += 'Buzz'
    if s == '':
        s = str(i)

    print (s)
