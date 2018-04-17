# Warmup-1 > sum_double
#
#  Given two int values, return their sum. Unless the two values are the same,
# then return double their sum.


def sum_double(a, b):
    if a == b:
        return 2 * (a + b)
    else:
        return a + b


sum_double(1, 2)

sum_double(2, 2)

# Warmup-1 > diff21
#
# Given an int n, return the absolute difference between n and 21, except
# return double the absolute difference if n is over 21.


def diff21(n):
    if n > 21:
        return 2 * abs(21 - n)
    else:
        return abs(21 - n)


diff21(5)

diff21(22)


# Warmup-1 > parrot_trouble
#
# We have a loud talking parrot. The "hour" parameter is the current hour
# time in the range 0..23. We are in trouble if the parrot is talking and
# the hour is before 7 or after 20. Return True if we are in trouble.

def parrot_trouble(talking, hour):
    if talking and (hour < 7 or hour > 20):
        return True
    else:
        return False


parrot_trouble(True, 6)

parrot_trouble(True, 7)

parrot_trouble(False, 6)


# Warmup-1 > makes10
#
# Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.


def makes10(a, b):
    if a == 10 or b == 10 or a + b == 10:
        return True
    else:
        return False


makes10(10, 20)
makes10(59, 9)
