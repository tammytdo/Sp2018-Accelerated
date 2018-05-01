#!/user/bin/env python

import re
from string import punctuation
import random


def parse_file(filename):
    with open(filename, 'r') as fin:
        for items in range(61):
            words = []
            word = []
            letter = ''
            for line in fin:
                for word in line:
                    for char in word:
                        letter = ''.join(char for char in line if char
                                         not in punctuation)
                word = re.split('\n| |-', letter)
                words.extend(word)
            for item in words:
                if item == '':
                    words.remove('')
            return words
        #  Can't figure out how to keep words that have '-' seperated. Tried
        #  "if char = '--' replace with ' ', but it would not incorporate it
        #  into "letter"


def build_trigram(words):  # works
    #  Brings in list from parse_file and builds Trigram Dictioanry
    trigram = {}  # dictionary
    for i in range(len(words) - 2):
        first = words[i]
        second = words[i + 1]
        third = words[i + 2]
        pair = (first, second)
        trigram.setdefault(pair, []).append(third)
        #  searches dictionary keys for 'pair' if not present, adds 'pair' as
        #  key, [empty] as values, then adds 'third' to the [empty].  If 'pair'
        #  is found, then adds 'third' to the already populated value.
    return trigram


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
    words = parse_file('sherlock_All.txt')
    trigram = build_trigram(words)
    text = make_new_text(trigram)
    print(text)
