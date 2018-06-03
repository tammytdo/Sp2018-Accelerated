#!/usr/bin/env Python
"""
trigrams:

solutions to trigrams
"""
import random
import re

sample = """Now is the time for all good men to come to the aid of the country"""

words = sample.split()

#print(words)

def parse_file(filename):
    """
    parses a text file to make a list of words
    """
    words = []
    with open(filename) as infile:
        for _ in range(68):
            infile.readline()
        for line in infile:
            if line.startswith("End of the Project"):
                break
#            print(line)
#           Borrowed Andy Kwon's awesome regex solution using re.findall (see journal)                
            wrds = re.findall("[\w']+|[.,!?:]", line)
            print(wrds)
            words.extend(wrds)
        return words

def build_trigram(words):
    '''Takes a string, splits it into words and creates a dictionary of three adjacent words.
    '''
    tris = {}
    for i in range(len(words)-2):
#        first = wrds[i]
#        second = wrds[i + 1]
#        third = wrds[i + 2]
#        combo = first + " " + second
#        tris.setdefault(pair, [])
#        tris[combo].append(third)
        pair = tuple(words[i:i+2])
        third = words[i+2]
        
        add_next = tris.setdefault(pair, [])
        add_next.append(third)
        
    return tris

def make_new_tris(trigram):
    '''Chooses a random pair from a list and generates a new tuple of random pairs'''
    pair = random.choice(list(trigram.keys()))
    sentence = []
    sentence.extend(pair)
    for i in range(30):
        nexttuple = trigram[pair]
        sentence.append(random.choice(nexttuple))
        pair = tuple(sentence[-2:])
#        print(pair)
    return sentence



if __name__ == "__main__":
    words = parse_file("sherlock.txt")
#    print(words)
    trigram = build_trigram(words)
    text = make_new_tris(trigram)
    print(text)
