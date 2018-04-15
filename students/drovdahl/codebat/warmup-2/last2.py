#! /usr/local/bin/python3


def last2(str):
    last2 = str[-2:]
    substr = ''
    x = 0
    for i in range(len(str) - 2):
        substr = str[i:i + 2]
        if substr == last2:
            x = x + 1
    return x
