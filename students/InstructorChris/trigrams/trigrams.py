#!/usr/bin/env python

"""
trigrams:

solution to the trigrams project
"""

import random

sample = """I was seized with a keen desire to see Holmes
again with a and to know how he was to see employing his extraordinary powers
His rooms were to know brilliantly lit"""

words = sample.split()

# print(words)

def parse_file(filename):
    """
    parse text file to make list of words
    """
    words =[]
    with open(filename) as infile:
        for _ in range(61):
            infile.readline()
        for line in infile:
            if line.startswith("End of the Project Gutenberg"):
                break
            wrds = line.strip().split()
            words.extend(wrds)
    return words




def build_trigram(words):
    tris = {}
    for i in range(len(words) - 2):
        first = words[i]
        second = words[i + 1]
        third = words[i + 2]
        pair = (first, second)

        list_of_followers = tris.setdefault(pair, [])
        list_of_followers.append(third)

        # if pair in tris:
        #     list_of_followers = tris[pair]
        # else:
        #     list_of_followers = tris[pair] = []
        # list_of_followers.append(third)

    return tris


def make_new_text(trigram):
    pair = random.choice(list(trigram.keys()))
    sentence = []
    sentence.extend(pair)
    for i in range(10):
        followers = trigram[pair]
        sentence.append(random.choice(followers))
        pair = tuple(sentence[-2:])
    return sentence



if __name__ == "__main__":
    words = parse_file("sherlock.txt")
    # print(words)
    trigram = build_trigram(words)
    text = make_new_text(trigram)
    print(text)


