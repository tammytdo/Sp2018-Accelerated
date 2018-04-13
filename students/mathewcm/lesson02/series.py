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
