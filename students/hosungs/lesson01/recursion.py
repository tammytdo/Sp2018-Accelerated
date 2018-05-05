def fact(n):
    '''
    Compute the factorial of n

    :param: n 
    :return:
    '''
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

