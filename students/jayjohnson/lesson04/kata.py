'''
Jay Johnson
Kata assignment
'''
#!/usr/bin/env python

import random
import string

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
            # remove symbols here
            #print(string.punctuation)
            wrds = [''.join(c for c in s if c not in string.punctuation) for s in wrds]
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
    return tris

def make_new_text(trigram):
    pair = random.choice(list(trigram.keys()))
    sentence = []
    sentence.extend(pair)
    for i in range(200):
        followers = trigram[pair]
        sentence.append(random.choice(followers))
        pair = tuple(sentence[-2:])
    return sentence

if __name__ == "__main__":
    words = parse_file("sherlock.txt")
    trigram = build_trigram(words)
    text = make_new_text(trigram)
    print(text)
