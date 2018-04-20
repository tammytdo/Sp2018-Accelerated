
"""
trigrams:

solutions to the trigrams project

"""
sample = """I was seized with a keen desire to see Holmes
again and to know how he was to see employing his extraordinary powers
His rooms were to know brilliantly lit"""

words = sample.split()

import random

print(words)

def parse_file(filename):
    """
    parse text file to makelist of words
    """
    words = []
    with open(filename) as infile:
        for _ in range(61):
            infile.readline()
        for line in infile:
            if line.startswith() == "End of the Project Gutenberg":
                break
            wrds = line.split().split()
            print(wrds)
            words.extend(wrds)
        return words


def build_trigrams(words):
    tris = {}
    for i in range(len(words) - 2):
        first = words[i]
        second = words[i + 1]
        third = words[i + 2]
        print(first, second, third)
        pair = (first, second)
        list_of_followers = tris.setdefault(pair, [])
        list_of_followers.append(third)
    print(tris)
    return tris


def make_new_text(trigram):
    pair = random.choice(list(trigram.keys()))
    sentence = []
    sentence.extend(pair)
    for i in range(10):
        followers = trigram[pair]
        sentence.append(random.choice(followers))
        pair = tuple(sentence [-2:])
        print(pair)
    return sentence


if __name__ == "__main__":
    words = parse_file("/Users/weepler/Python210/Sp2018-Accelerated/students/Wayne/Assignments/Lesson4/sherlock.txt")
    trigram = build_trigrams(words)
    make_new_text(trigram)
