#! /usr/local/bin/python3


def front_back(str):
    if len(str) > 1:
        newstr = (str[-1:] + str[1:len(str)-1] + str[0])
        return (newstr)
    else:
        return(str)
