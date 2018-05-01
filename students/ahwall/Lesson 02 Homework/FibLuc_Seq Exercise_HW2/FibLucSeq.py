def fibinacci(x):
    a = 0
    b = 1
    c = 0
    if (x == 0):
        print(x)
    else:
        for i in range(x):
            a = b
            b = c
            c = b + a
        print(c)


def lucas(x):
    a = 2
    b = 1
    if x == 0:
        print(2)
    elif x == 1:
        print(1)
    else:
        for i in range(2, x + 1):
            c = b + a
            a = b
            b = c
        print(c)


def sum_series(x, a = 0, b = 1):
    if (a == 2) and (b == 1):
        lucas(x)
    else:
        fibinacci(x)
