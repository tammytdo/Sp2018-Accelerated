#! /usr/local/bin/python3


def parrot_trouble(talking, hour):
    if hour < 7 or hour > 20:
        hour = True
    else:
        hour = False
    return ((talking and hour))
