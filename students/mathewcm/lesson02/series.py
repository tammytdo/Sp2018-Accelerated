def fibonacci(n):
    """
    This function will return the nth iteration of that value in the fibonacci sequence.
    """
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    # n > 2
    a = 1
    b = 1
    # First two members of the series
    series = [a, b]
    for i in range(n):
        c = a + b
        series.append(c)
        a = b
        b = c
    return series[-4]

def lucas(n):
    """
    This function will return the nth iteration of that value in the Lucas sequence.
    """
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    # n > 2
    a = 1
    b = 3
    # First two members of the series
    series = [a, b]
    for i in range(n):
        c = a + b
        series.append(c)
        a = b
        b = c
    return series[-4]

def sum_series(n, a, b):
    """
    This function is a generalization of the fibonacci sequence and the Lucas sequence and defaults to the values of the fibonacci sequence if no optional inputs for a and b are entered. The function returns the nth value in the series.
    """
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    # n > 2
    if a is None:
        return a == 0
    if b is None:
        return b == 1
    # First two members of the series
    series = [a, b]
    for i in range(n):
        c = a + b
        series.append(c)
        a = b
        b = c
    return series[-4]
