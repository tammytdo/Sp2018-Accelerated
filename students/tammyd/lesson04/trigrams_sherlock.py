#!/usr/local/bin/python

"""

trigrams: sherlock holmes

"""

import random

# sample = """ "Not a bit, Doctor. Stay where you are. I am lost without my
# Boswell. And this promises to be interesting. It would be a pity
# to miss it." """

# words = sample.split()
# print(words)


# def build_trigram(words):
#     tris = {}
#     for i in range(len(words)-2):
#         first = words[i]
#         second = words[i + 1]
#         third = words[i + 2]
#         print(first, second, third)
#         pair = (first, second)
#         tris.setdefault(pair, []).append(third)

#     print(tris)
#     return tris


def parse_file(filename):
    """
    parse text file to make list of words
    """
    words = []
    with open(filename) as infile:
        for _ in range(61):
            infile.readline()
        for line in infile:
            if line ==  "End of the Project Gutenberg":
                break
            wrds = line.strip().split()
            print(wrds)
            words.extend(wrds)
        print(words)


def build_trigram(words):
    tris = {}

def make_new_text(trigram):
    pair = random.choice(list(trigram.keys()))
    sentence = []
    sentence.extend(pair)
    for i in range(10):
        followers = trigram[pair]
        sentence.append(random.choice(followers))
        pair =  tuple(sentence[-2:])
        result = ' '.join(sentence).capitalize().replace(' i ', ' I ')+"."
    return sentence


if __name__ == '__main__':
    words = parse_file("/Users/tammydo/Sp2018-Accelerated/students/tammyd/lesson04/sherlock.txt")
    trigram = build_trigram
    sentence = make_new_text
