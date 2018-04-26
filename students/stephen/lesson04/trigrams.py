#!/usr/bin/env python

"""
trigrams
part 1: read the text file and transform into list of words
part 2: process the words to create trigrams
part 3: use those trigrams to create new text
"""

# sample = """One night--it was on the twentieth of March, 1888--I was
# returning from a journey to a patient (for I had now returned to
# civil practice), when my way led me through Baker Street. As I
# passed the well-remembered door, which must always be associated
# in my mind with my wooing, and with the dark incidents of the
# Study in Scarlet, I was seized with a keen desire to see Holmes
# again, and to know how he was employing his extraordinary powers.
# His rooms were brilliantly lit, and, even as I looked up, I saw
# his tall, spare figure pass twice in a dark silhouette against
# the blind. He was pacing the room swiftly, eagerly, with his head
# sunk upon his chest and his hands clasped behind him. To me, who
# knew his every mood and habit, his attitude and manner told their
# own story. He was at work again. He had risen out of his
# drug-created dreams and was hot upon the scent of some new
# problem. I rang the bell and was shown up to the chamber which
# had formerly been in part my own.
# """

# words = sample.split()

# print(words)

import random

def parse_file(filename):
    """
    Parse text file to make list of words.
    """
    with open(filename) as infile:
        words = []  # start with empty list
        for i in range(60):
            infile.readline()
        for line in infile:
            if line.startswith("End of the Project Gutenberg"):
                break
            # print(line)
            words.extend(line.split())
    return words


def build_trigram(words):
    tris = {}
    for i in range(len(words) - 2):
        first = words[i]
        second = words[i + 1]
        third = words[i + 2]
        # print(first, second, third)
        pair = (first, second)
        tris.setdefault(pair, []).append(third)
        # if you want a unique list of words after the pairs, use a set
    return tris

def make_new_text(trigram, length=1000):
    pair = random.choice(list(trigram.keys()))
    sentence = []
    sentence.extend(pair)
    while not (len(sentence) >= length and sentence[-1][-1] == '.'):
        followers = trigram[pair]
        sentence.append(random.choice(followers))
        pair = tuple(sentence[-2:])
    new_text = ''
    for word in sentence:
        new_text += word + ' '
    new_text = new_text[:-1]
    new_text = new_text[0].capitalize() + new_text[1:]
    return new_text


if __name__ == "__main__":
    words = parse_file("sherlock.txt")
    trigram = build_trigram(words)
    new_text = make_new_text(trigram, 500)
    print(new_text)
