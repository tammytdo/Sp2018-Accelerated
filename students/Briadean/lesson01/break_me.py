#!/usr/bin/env python
"""Script to demonstrate various common built in exceptions within Python"""

def generate_name_error():
    x = 1 + yellow
    return x


def generate_type_error(x, y):
    x = x + y
    return x


def generate_syntax_error():
    x = print "Bananas!"
    return x


def generate_attribute_error(list_a, list_b):
    both = list_a.intersection(list_b)
    return both



fruit_list = ["apple", "banana", "strawberry", "tomato"]
vegetable_list = ["pumpkin", "pea", "carrot", "tomato"]

if __name__ == "__main__":

    # generate_name_error()
    # generate_type_error(1, fruit_list)
    # generate_syntax_error()
    # generate_attribute_error(fruit_list, vegetable_list)
