#! /usr/local/bin/python3


def not_string(str):
    if str.startswith('not'):
        return str
    else:
        return ('not ' + str)
