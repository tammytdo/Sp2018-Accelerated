#!/usr/bin/env python

"""
trigrams:

solution to the trigrams project
"""
sample = """I was seized with a keen desire to see Holmes
again with a and to know how he was to see employing his extraordinary powers
His rooms were to know brilliantly lit"""

words = sample.split()

print(words)

def parse_file(filename):
    """
    parse text file to make list of words
    """
    with open(filename) as infile:
        words =[]
        for line in infile:
            wrds = line.strip().split()
            words.extend(wrds)
    return words


def build_trigram(words):
    tris = {}
    for i in range(len(words) - 2):
        first = words[i]
        second = words[i + 1]
        third = words[i + 2]
        print(first, second, third)
        pair = (first, second)

        list_of_followers = tris.setdefault(pair, [])
        list_of_followers.append(third)

        # if pair in tris:
        #     list_of_followers = tris[pair]
        # else:
        #     list_of_followers = tris[pair] = []
        # list_of_followers.append(third)

    print(tris)
    return tris

if __name__ == "__main__":
    words = parse_file("sherlock_small.txt")
    print(words)
    # trigram = build_trigram(words)

