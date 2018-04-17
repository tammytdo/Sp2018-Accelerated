#! /usr/local/bin/python3


def array_count9(nums):
    x = 0
    for i in nums:
        if i == 9:
            x = x + 1
    return x
