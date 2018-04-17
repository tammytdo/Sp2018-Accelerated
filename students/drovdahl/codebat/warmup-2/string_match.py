#! /usr/local/bin/python3


def string_match(a, b):
    x = 0
    if len(a) >= len(b):
        for i in range(len(b)-1):
            substr1 = a[i] + a[i+1]
            substr2 = b[i] + b[i+1]
            if substr1 == substr2:
                x = x + 1
    else:
        for i in range(len(a)-1):
            substr1 = a[i] + a[i+1]
            substr2 = b[i] + b[i+1]
            if substr1 == substr2:
                x = x + 1
    return x
