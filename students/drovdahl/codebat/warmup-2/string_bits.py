#! /usr/local/bin/python3


def string_bits(str):
    newstr = ''
    x = len(str)
    for i in range(x):
        if i % 2 == 0:
            newstr = newstr + str[i]
    return newstr
