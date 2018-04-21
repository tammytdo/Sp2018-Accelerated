
"""
trigrams:
"""

import random


def parse_file(filename):
    """
    parse text file to makelist of words
    """
    words = []
    with open(filename) as infile:
        for _ in range(61):
            infile.readline()
        for line in infile:
            if line.startswith("End of the Project Gutenberg"):
                break
            wrds = line.strip().split()
            words.extend(wrds)
        return words

    """
    Creates a dictionary for tris and then sets the key for the
    dictionary by using the set default method.
    """


def build_trigrams(words):
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
    for i in range(10):
        followers = trigram[pair]
        sentence.append(random.choice(followers))
        pair = tuple(sentence[-2:])
    return sentence


if __name__ == "__main__":
    words = parse_file("/Users/weepler/Python210/Sp2018-Accelerated/students/Wayne/Assignments/Lesson4/sherlock.txt")
    trigram = build_trigrams(words)
    text = make_new_text(trigram)
    print(text)
