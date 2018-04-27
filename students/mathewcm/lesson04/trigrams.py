#!/usr/bin/env Python
"""
trigrams:

solutions to trigrams
"""
sample = """Now is the time for all good men to come to the aid of the country"""

import random

words = sample.split()

print(words)

def parse_file(filename)
    """
    parse text file to makelist of words
    """
    with open(filename) as infile:
        words = []
        for line in infile:
            print(line)
            wrds = line.strip().split()
#            print(wrds)
            words.extend(wrds)

        return words

def build_trigram(words):
    tris = {}
    for i in range(len(words) - 2):
        first = words[i]
        second = words[i + 1]
        third = words[i + 2]
#        print(first, second, third)
        tris[(first, second)] = [third]

#    print(tris)
    return tris

def make_new_text(trigram)
    pair = random.choice(list(trigram.keys()))
    sentence = []
    sentence.extend(pair)
    for i in range(10):
        followers = trigram[pair]
        sentence.append(random.choice(followers))
        pair = tuple(sentence[-2])
        print(pair)
    return sentence



if __name__ == "__main__"
    words = parse_file("sherlock_small.txt")
    print(words)
#    trigram = build_trigram(words)
