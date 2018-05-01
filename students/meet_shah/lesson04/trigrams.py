#!/usr/bin/env python

"""
trigrams:

Let's do trigrams!
"""

import random

def parse_file(filename):
    words = []
    with open(filename) as infile:
        for _ in range(61):
            infile.readline()
        for line in infile:
            word_in_line = line.strip().split()
            #print(word_in_line)
            words.extend(word_in_line)
            if line.startswith("End of the Project Gutenberg"):
                break
    return words


def build_trigrams(words):
    tris = {}
    for i in range(len(words)-2):
        pair = (words[i], words[i+1])
        third = words[i+2]
        tris.setdefault(pair, []).append(third)

    return tris

def make_new_text(trigram):
    punctuation = [',', '.', '.', '.', '.', '.', '?', '!']
    pair = random.choice(list(trigram.keys()))
    sentence = []
    sentence.extend(pair)
    sentence_length = random.randint(5,15)
    for i in range(sentence_length):
        followers = trigram[pair]
        sentence.append(random.choice(followers))
        pair = tuple(sentence[-2:])
    mysentence = " ".join(sentence) + random.choice(punctuation)
    return mysentence[0].upper() + mysentence[1:]

if __name__ == "__main__" :
    words = parse_file("./sherlock.txt")
    trigram = build_trigrams(words)
    sentence = make_new_text(trigram)
    print(sentence)
    #print(trigram)
