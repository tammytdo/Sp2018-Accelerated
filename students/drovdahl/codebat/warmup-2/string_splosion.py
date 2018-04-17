#! /usr/local/bin/python3


def string_splosion(str):
    newstr = ''
    for i in range(len(str)):
        newstr = newstr + str[0:i+1]
    return newstr
