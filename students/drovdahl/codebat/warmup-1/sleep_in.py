#! /usr/local/bin/python3


def sleep_in(weekday, vacation):
    if vacation or not weekday:
        return True
    else:
        return False


sleep_in(False, True)
