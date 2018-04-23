#! /usr/local/bin/python3


'''
Perform a number of string formatting exercises
'''


def task_1():
    '''
    produce 'file_002 :   123.46, 1.00e+04, 1.23e+04'
    '''
    seq = (2, 123.4567, 10000, 12345.67)
    fname = seq[0]
    number1 = seq[1]
    number2 = seq[2]
    number3 = seq[3]
    print(f'file_{fname:0>3d}:  {number1:.2f}, {number2:.2e}, {number3:.2e}')


def task_2():
    '''
    produce the same results as task_1 using an alternate type of format string
    '''
    seq = (2, 123.4567, 10000, 12345.67)
    print('\n\n')
    print('file_{:0>3}:  {:.2f}, {:.2e}, {:.2e}'.format(seq[0], seq[1], seq[2],
          seq[3]))
    # here's a shortened version
    print('file_{:0>3}:  {:.2f}, {:.2e}, {:.2e}'.format(*seq))


def task_3(seq):
    '''
    rewrite "the 3 numbers are: {:d}, {:d}, {:d}".format(1,2,3)
    to take an arbitrary number of values.
    '''
    length = len(seq)
    values_list = ['{}'] * length
    values = ', '.join(values_list)
    print('\n\n')
    print(('the {} values are ' + values).format(length, *seq))


def task_4(seq):
    '''
    given tuple( 4, 30, 2017, 2, 27)
    use string formating to print:
    '02 27 2017 04 30'
    '''
    print('\n\n')
    print(f'{seq[3]:0>2d} {seq[4]:0>2d} {seq[2]} {seq[0]:0>2d} {seq[1]:0>2d}')


def task_5():
    '''
    Given list ['oranges', 1.3, 'lemons', 1.1]
    Write an f-string that will display:
    The weight of an orange is 1.3 and the weight of a lemon is 1.1
    Conclude by changing the f-string so that it displays the names of the
    fruit in upper case, and the weight 20% higher (that is 1.2 times higher).
    '''
    seq = ['oranges', 1.3, 'lemons', 1.1]
    f1 = seq[0]
    w1 = seq[1]
    f2 = seq[2]
    w2 = seq[3]
    print('\n\n')
    print(f'The weight of an {f1} is {w1} and the weight of a {f2} is {w2}')
    # change the fruit to uppercase and add %20 to the weight
    print(f'The weight of an {f1.upper()} is {w1 * 1.2} and the weight of a '
          f'{f2.upper()} is {w2 * 1.2}')


def task_6():
    '''
    Use string formatting to display data in columns
    '''
    seq0 = ('name', 'age', 'cost')
    seq1 = ('Mr Roboto', 56, 45000000)
    seq2 = ('6M Man', 78, 6000000)
    seq3 = ('Austin Powers', 128, 1000000)
    seq4 = ('Buzz Lightyear', 18, 19.95)
    # the name column will be 15 characters
    # the age and cost columns will each be 10 characters
    print('\n\n')
    print(f'{seq0[0]:^15}|{seq0[1]:^10}|  {seq0[2]:^10}')
    print(('_' * 15) + '|' + ('_' * 10) + '|' + ('_' * 12))
    print(f'{seq1[0]:<15}|{seq1[1]:^10}| ${seq1[2]:>10}')
    print(f'{seq2[0]:<15}|{seq2[1]:^10}| ${seq2[2]:>10}')
    print(f'{seq3[0]:<15}|{seq3[1]:^10}| ${seq3[2]:>10}')
    print(f'{seq4[0]:<15}|{seq4[1]:^10}| ${seq4[2]:>10}')


if __name__ == "__main__":
    task_1()
    task_2()
    task_3((1, 2, 3, 4, 5, 6))
    task_4((4, 30, 2017, 2, 27))
    task_5()
    task_6()
