#! /usr/local/bin/python3


def array_front9(nums):
    x = False
    end = len(nums)
    if end > 4:
        end = 4
    for i in range(end):
        if nums[i] == 9:
            x = True
    return x
